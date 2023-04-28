import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import storage
from . import app
from src.config import SECRET_KEY

config = {
    'apiKey': "AIzaSyAW8hNJncjK9AZtKrCeGjKRiiUbyA0XoXc",
    'authDomain': "travelblog-b7941.firebaseapp.com",
    'projectId': "travelblog-b7941",
    'storageBucket': "travelblog-b7941.appspot.com",
    'messagingSenderId': "839540723786",
    'appId': "1:839540723786:web:1bef7981791d6bdbd396b3",
    'measurementId': "G-G30PEKM6W4",
    'databaseURL': ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# db = firebase.database()

# storage = firebase.storage()

app.secret_key = SECRET_KEY  # change for real secret


def getAuth():
    return auth


cred = credentials.Certificate("src/secret.json")
firebase_auth = firebase_admin.initialize_app(
    cred, {'storageBucket': "travelblog-b7941.appspot.com"})

db = firestore.client()
# data = {"title": "Italy trip", "author": "John Smith", "hashtag": "#Italy",
#         "photoUrl": "https://images.pexels.com/photos/2064827/pexels-photo-2064827.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"}
# doc_ref = db.collection('posts').document()
# doc_ref.set(data)


# Opt : if you want to make public access from the URL
# blob.make_public()


def getDb():
    return db


# fileName = "E:/masterThesisProjects/travelBlogFlask/src/tree.jpg"
bucket = storage.bucket()
# blob = bucket.blob('images')
# blob.upload_from_filename(fileName)
# print("uploaded")


def getBucket():
    return bucket
# def getStorage():
#     return storage
