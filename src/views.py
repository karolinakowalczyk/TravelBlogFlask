from flask import Flask, send_from_directory, session, render_template, request, redirect, flash, url_for

from . import app
from .firebaseConfig import getAuth
from .firebaseConfig import getDb
from flask_uploads import IMAGES, UploadSet, configure_uploads

from src.forms.registrationForm import RegistrationForm
from src.forms.addPostForm import AddPostForm

from werkzeug.utils import secure_filename


auth = getAuth()
db = getDb()

# app.config["UPLOADED_PHOTOS_DEST"] = 'uploads'
app.config["UPLOADED_PHOTOS_DEST"] = 'src/static/uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
# for post in posts:
#     print(post.id)
#     print(post.to_dict())
#     posts.append(post.to_dict())


@app.route("/", methods=['POST', 'GET'])
def home():
    if ('user' in session):
        print('Hi, {}'.format(session['user']))

    return render_template('home.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    registerForm = RegistrationForm(request.form)
    if request.method == 'POST' and registerForm.validate():
        # email = request.form.get('email')
        # password = request.form.get('password')
        email = registerForm.email.data
        password = registerForm.password.data
        print("form valid")
        try:
            auth.create_user_with_email_and_password(email, password)
            print('Register successfully')
            return redirect('/login')
        except:
            print(auth.current_user)
            print('Failed to register')
            return redirect('/register')

    return render_template('register.html', registerForm=registerForm)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            auth.sign_in_with_email_and_password(email, password)
            session['user'] = auth.current_user['localId']
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

    # nie widzi user id
    userPosts = db.collection('posts').where(
        'userId', "==", session['user']).get()
    userPostsData = []
    print(userPosts)
    for post in userPosts:
        # print(post.id)
        # print(post.to_dict())
        userPostsData.append(post.to_dict())
    # for p in userPostsData:
    #     print(p["title"])
    # print(userPostsData)
    return render_template('my-posts.html', userPostsData=userPostsData)

# TODOHow make it better?


hashtags = []


@app.route('/add-hashtag', methods=['POST'])
def addHashtag():
    global hashtags
    hashtag = request.get_json()
    hashtags.append(hashtag['hashtag'])
    print("add hashtag")
    print(hashtags)
    return hashtags


@app.route('/remove-hashtag', methods=['POST'])
def removeHashtag():
    global hashtags
    hashtag = request.get_json()
    hashtags.remove(hashtag['hashtag'])
    print("remove hashtag")
    print(hashtags)
    return hashtags


# @app.route('/upload-image', methods=['POST', 'GET'])
# def uploadImage():
#     uploadImageForm = UploadImageForm()
#     print('upload image')

#     if uploadImageForm.validate():
#         filename = photos.save(uploadImageForm.photo.data)
#         fileUrl = url_for('getFile', filename)
#     else:
#         fileUrl = None
#     return render_template('upload-image.html', uploadImageForm=uploadImageForm, fileUrl=fileUrl)

# filenames = []

@app.route('/uploads/<filename>')
def getFile(filename):
    return send_from_directory(app.config["UPLOADED_PHOTOS_DEST"], filename)


@app.route("/add-post", methods=['POST', 'GET'])
def addPost():
    global fileUrl
    fileUrl = None
    # addPostForm = AddPostForm(request.form)
    addPostForm = AddPostForm()

    if request.method == 'POST' and addPostForm.validate():
        addSubmit = request.form.get("add")
        uploadSubmit = request.form.get("upload")
        print("POST method")
        if uploadSubmit is not None:
            print("add photo")

            image = addPostForm.images.data
            print(image)
            if image is not None:
                filename = photos.save(image)
                fileUrl = url_for('getFile', filename=filename)
            else:
                fileUrl = None
            # filenames.append(filename)

            # for image in addPostForm.images.data:
            #     filename = photos.save(image)
            #     filenames.append(filename)

        elif addSubmit is not None:
            # print(addPostForm.title.data)
            # print(addPostForm.title)
            # print("-----")

            # print("addsubmit")
            # print(addSubmit)
            # print("uploadsubmit")
            # print(uploadSubmit)

            global hashtags
            # print("HASHTAGS")
            # print(hashtags)
            data = {"userId": session['user'], "title": addPostForm.title.data,
                    "author": addPostForm.author.data, "hashtags": hashtags}

            db.collection('posts').document().set(data)
            hashtags = []

            # message = "Your post was added!"
            return redirect('/my-posts')

    else:
        print("Fill all required fields")
        # message = "Fill all required fields"
    print("fileUrl")
    print(fileUrl)
    return render_template('add-post.html', addPostForm=addPostForm, fileUrl=fileUrl)
