from flask import Flask,render_template,url_for,escape,request,redirect,flash,logging
from helpers.db_crud import *
from helpers.auth_helpers import *
from model.authmodel import *
from model.form import *

app = Flask(__name__)
app.secret_key="library"

@app.route('/')
@role_required()
def Index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
@login_required
def Login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        login = LoginModel(form.username.data,form.password.data)
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
        register = RegisterModel(form.username.data,form.password.data,form.role.data)
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

@app.route("/searchuser",methods=["GET","POST"])
@role_required(role = 'User')
def searchUser():
    return "searchuser"

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