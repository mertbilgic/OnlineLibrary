from flask import Flask,render_template,url_for,escape,request,redirect,flash,logging
from helpers.json_helper import *
from helpers.auth_helpers import *
from helpers.lib_tans_helper import *
from helpers.file_upload_helpers import *
from helpers.image_proc_helpers import *
from model.authmodel import *
from model.bookmodel import *
from model.form import *
import uuid

app = Flask(__name__)
app.secret_key = "12312313"#uuid.uuid4().hex
app.config['UPLOAD_FOLDER'] = FileUpload.UPLOAD_FOLDER

@app.route('/index')
@role_required()
def Index():
    form = SearchForm(request.form)
    return render_template("index.html",form=form)

@app.route("/",methods=["GET","POST"])
@login_required
def Login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = get_sha256_password(form.password.data)
        login = LoginModel(form.username.data,hashed_password)
        result = Database.find_one("Users",login.__dict__)
        if bool(result):
            _id = JSONEncoder().encode(result['_id'])
            session_openned(_id,result['username'],result["role"])
            #flash("Kullanıcı Girişi Başarılı","success")
            return redirect(url_for('Index'))
    return render_template("login.html",form=form)

@app.route("/signup",methods=["GET","POST"])
@login_required
def SingUp():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = get_sha256_password(form.password.data)
        register = RegisterModel(form.username.data,hashed_password,form.role.data)
        Database.insert("Users",register.__dict__)
        flash("Kayıt İşlemi Başarılı","success")
        return redirect(url_for('Login'))
    return render_template("signup.html",form=form)

@app.route("/logout")
@logout_required
def Logout():
    session_closed()
    return redirect(url_for('Login'))

@app.route("/addbook",methods=["GET","POST"])
@role_required(role = 'Admin')
def addBook():
    session['url'] = 'addBook'
    form = BookForm(request.form)
    if 'isbn' in session:
        form.ISBN.data = session['isbn']
    if request.method == 'POST' and form.validate():
        book = BookModel(form.book_name.data,form.ISBN.data)
        book_data = book.__dict__
        book_data.update({"added_user_id":session['_id']})
        Database.insert("Books",book_data)
        del session['isbn']

    return render_template('addbook.html',form=form)

@app.route("/uploadfile",methods=["GET","POST"])
@role_required()
def uploadFile():
    if request.method == 'POST':
        #https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
        if 'file' not in request.files:
            flash('No file part',"danger")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file',"danger")
            return redirect(request.url)
        if file and FileUpload.allowed_file(file.filename):
            FileUpload.FILE_NAME = file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = FileUpload.UPLOAD_FOLDER + FileUpload.FILE_NAME
            imgproc = ImageProc(path)
            session['isbn'] = imgproc.get_result()
        flash(file.filename+' adlı dosya kayıt edildi','success')
        return redirect(url_for(session['url']))
    return redirect(url_for('Index'))

@app.route("/listuser",methods=["GET","POST"])
@role_required(role = 'Admin')
def listUser():
    user_info = Database.aggregate("Users","RentBooks","username","renter_user")
    return render_template('listuser.html',user_info=user_info)

@app.route("/extenddate",methods=["GET","POST"])
@role_required(role = 'Admin')
def extendDate():
    return "extendthedate"

@app.route("/changelocaldate",methods=["GET","POST"])
@role_required(role = 'Admin')
def changeLocalDate():
    form = CTimeForm(request.form)
    if request.method == 'POST':
        day = form.day.data
        if len(day):
            Date.next_day += int(form.day.data)
        else: 
            Date.next_day += 20
        flash("Sistem Tarihi: {}".format(Date.get_date_time()),"success")
    return render_template('changelocaldate.html',form=form)

@app.route("/searchbook",methods=["GET","POST"])
@role_required(role = 'User')
def searchBook():
    keyword = request.form.get("search",None)
    form = SearchForm(request.form)
    books = []

    if keyword == '' :
        flash("Lütfen input alanına veri giriniz","danger")
    elif keyword != None : 
        query = {"$search" :"(\"{}\"".format(keyword)}
        books = Database.find("Books",{ "$text": query})
        
        if bool(books): flash("Aradığınız kitap mevcut değil","info")

    return render_template('listbook.html',books=books,form=form)

@app.route("/rentbook",methods=["GET","POST"])
@role_required(role = 'User')
def rentbook():
    ISBN = request.args.get('ISBN')
    if ISBN != None:
        message,result = rent_book(ISBN,session['username'])
        flash(message,result)
    books = Database.find_all("Books")
    return render_template('rentbook.html',books=books)

@app.route("/deliverbooks",methods=["GET","POST"])
@role_required(role = 'User')
def deliverBooks():
    session['url'] = 'deliverBooks'
    form = BookForm(request.form)
    if 'isbn' in session:
        form.ISBN.data = session['isbn']
        del session['isbn']
    ISBN = request.args.get('ISBN',form.ISBN.data)
    if request.method == 'POST' and form.validate() and ISBN != '':
        message,result = Database.deliver_book('RentBooks','Books',{"ISBN":ISBN})
        flash(message,result)
    books = Database.find("RentBooks",{ "renter_user":session['username']})
    return render_template('deliverbooks.html',books=books,form=form)

#debug=true modunda hata çalıştırıldığında hata ile karşılaşabilirsiniz
if __name__=="__main__":
    app.run(debug=True)