from flask import Flask,render_template,url_for,escape,request,redirect,flash,session,logging
from helpers.db_crud import *
from model.authmodel import *
from model.form import *

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def Login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        login = LoginModel(form.username.data,form.password.data)
        if Database.find("Users",login.__dict__).count() == 0:
            print("Kullanıcı yok")
        else:
            print("Hoşgeldin",login.__dict__.get("username", ""))
    return render_template("login.html",form=form)

@app.route("/signup",methods=["GET","POST"])
def SingUp():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        register = RegisterModel(form.username.data,form.password.data,form.role.data)
        print(register.__dict__)
        Database.insert("Users",register.__dict__)
    return render_template("signup.html",form=form)

#debug=true modunda hata çalıştırıldığında hata ile karşılaşabilirsiniz
if __name__=="__main__":
    app.run(debug=True)