from flask import Flask, request, render_template, make_response, redirect
from functools import wraps
from authenticator import generate_token, isTokenValid

app = Flask(__name__)

def tokenValidation(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.cookies.get('access_token')
        if not isTokenValid(access_token):
            return redirect("bad request"), 403
        return f(*args,**kwargs)
    return decorated_function

@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return "bad request", 402

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        if userValidation(user,password):
            response = make_response(redirect('/Youtube'))
            response.set_cookie('access_token', generate_token(user))
            return response
        else:
            return "Error de credenciales", 402
    return "bad request", 402

@app.route('/youtube')
@tokenValidation
def page():
    if request.method == 'GET':
        return redirect('https://www.youtube.com/')
    
@app.route('/gmail')
@tokenValidation
def page2():
    if request.method == 'GET':
        return redirect('https://mail.google.com/')


def userValidation(user, password):
    if user=="admin" and password=="admin":
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(port = 5000)