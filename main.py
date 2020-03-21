from flask import Flask,render_template,url_for,escape,request,redirect,flash,logging
from helpers.db_crud import *
from helpers.auth_helpers import *
from model.authmodel import *
from model.form import *

app = Flask(__name__)
app.secret_key="library"

@app.route('/')
@login_required(None)
def Index():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
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
def SingUp():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        register = RegisterModel(form.username.data,form.password.data,form.role.data)
        Database.insert("Users",register.__dict__)
    return render_template("signup.html",form=form)

#debug=true modunda hata çalıştırıldığında hata ile karşılaşabilirsiniz
if __name__=="__main__":
    app.run(debug=True)