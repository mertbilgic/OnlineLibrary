from flask import Flask,render_template,url_for,escape,request,redirect,flash,session,logging

app = Flask(__name__)


@app.route('/')
def Index():
    return render_template("index.html")

@app.route('/login')
def Login():
    return render_template("login.html")



#debug=true modunda hata çalıştırıldığında hata ile karşılaşabilirsiniz
if __name__=="__main__":
    app.run(debug=True)