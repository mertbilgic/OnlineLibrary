from functools import wraps,partial,update_wrapper
from flask import url_for,session,redirect
from hashlib import sha256


def role_required(role = None):
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
        
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return f(*args, **kwargs)
        else:
            #flash("Kullanıcı girişi yapmanız gerekiyor.","danger")
            return redirect(url_for('Index'))
    return decorated_function

def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" in session:
            return f(*args, **kwargs)
        else:
            #flash("Kullanıcı girişi yapılmadı.","danger")
            return redirect(url_for('Index'))
    return decorated_function

def session_openned(username,role):

    session["username"] = username
    session["role"] = role

def session_closed():

    del session["username"]
    del session["role"]

def get_sha256_password(password):
    hashed_password = sha256(password.encode('ascii')).hexdigest()
    return hashed_password
  