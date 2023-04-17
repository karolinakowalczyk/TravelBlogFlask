from flask import Flask, session, render_template, request, redirect
from . import app
from .firebaseConfig import getAuth

@app.route("/", methods=['POST', 'GET'])
def home():
    loggedUser = False
    if('user' in session):
        print('Hi, {}'.format(session['user']))
        loggedUser = True
    return render_template('home.html', loggedUser=loggedUser)

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth = getAuth()
            auth.create_user_with_email_and_password(email, password)
            print('Register successfully')
            return redirect('/login')
        except:
            print(auth.current_user)
            print ('Failed to register')
            return redirect('/register')

    return render_template('register.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth = getAuth()
            auth.sign_in_with_email_and_password(email, password)
            #print(auth.current_user)
            session['user'] = email
            print('Log in successfully')
            return redirect('/')
        except:
            print(auth.current_user)
            print ('Failed to log in')
            return redirect('/login')

    return render_template('login.html')

@app.route('/logout')
def logout():
    if session.get('user') != None:
        session.pop('user')  
        print("Log out successfully")     
    return redirect('/')



        

# @app.route("/about/")
# def about():
#     return render_template("about.html")

# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")

# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello_there(name = None):
#     return render_template(
#         "hello_there.html",
#         name=name,
#         date=datetime.now()
#     )

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")
