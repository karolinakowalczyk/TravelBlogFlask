from flask import Flask, session, render_template, request, redirect
from . import app
from .firebaseConfig import getAuth
from .firebaseConfig import getDb


auth = getAuth()
db = getDb()


@app.route("/", methods=['POST', 'GET'])
def home():
    loggedUser = False
    if ('user' in session):
        print('Hi, {}'.format(session['user']))
        loggedUser = True
    return render_template('home.html', loggedUser=loggedUser)


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth.create_user_with_email_and_password(email, password)
            print('Register successfully')
            return redirect('/login')
        except:
            print(auth.current_user)
            print('Failed to register')
            return redirect('/register')

    return render_template('register.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth.sign_in_with_email_and_password(email, password)
            # print(auth.current_user)
            session['user'] = email
            print('Log in successfully')
            return redirect('/')
        except:
            print(auth.current_user)
            print('Failed to log in')
            return redirect('/login')

    return render_template('login.html')


@app.route('/logout')
def logout():
    if session.get('user') != None:
        session.pop('user')
        print("Log out successfully")
    return redirect('/')


@app.route("/my-posts", methods=['POST', 'GET'])
def myPosts():
    return render_template('my-posts.html')


@app.route("/add-post", methods=['POST', 'GET'])
def addPost():
    data = {"title": request.form.get(
        'title'), "author": request.form.get('author')}
    doc_ref = db.collection('posts').document()
    doc_ref.set(data)

    return render_template('add-post.html')
