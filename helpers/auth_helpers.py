from flask import url_for,session,redirect
from functools import wraps,partial,update_wrapper

def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "role" not in session:
                return redirect(url_for('Login'))
            if session["role"] == role or role == None:
                return f(*args, **kwargs)
            else:
                #flash("Yetkisiz Alan","danger")
                return redirect(url_for('Index'))
            return f(*args, **kwargs)
        return update_wrapper(decorated_function, f)
    return decorator

def session_openned(username,role):

    session["username"] = username
    session["role"] = role

    auth_decorator = partial(login_required,role = role)

def session_closed():

    if session.get("username") :

        del session["username"]
        del session["role"]
        print("Session temizlendi")
    else:
        print("Çıkış yapıcak kullanıcı yok")

