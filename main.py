from flask import Flask,render_template,url_for,escape,request,redirect,flash,logging
from helpers.db_crud import *
from helpers.auth_helpers import *
from model.authmodel import *
from model.form import *
import uuid

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex

@app.route('/')
@role_required()
def Index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
@login_required
def Login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = get_sha256_password(form.password.data)
        login = LoginModel(form.username.data,hashed_password)
        result = Database.find_one("Users",login.__dict__)
        if bool(result):
            session_openned(result['username'],result["role"])
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
    return "addbook"

@app.route("/listuser",methods=["GET","POST"])
@role_required(role = 'Admin')
def listUser():
    return "listuser"

@app.route("/extenddate",methods=["GET","POST"])
@role_required(role = 'Admin')
def extendDate():
    return "extendthedate"

@app.route("/searchbook",methods=["GET","POST"])
@role_required(role = 'User')
def searchUser():
    return "searchbook"

@app.route("/rentbook",methods=["GET","POST"])
@role_required(role = 'User')
def addtime():
    return "rentbook"

@app.route("/deliverbooks",methods=["GET","POST"])
@role_required(role = 'User')
def deliverBooks():
    return "deliverbooks"

#debug=true modunda hata çalıştırıldığında hata ile karşılaşabilirsiniz
if __name__=="__main__":
    app.run(debug=True)