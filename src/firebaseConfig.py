import pyrebase
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

app.secret_key =  SECRET_KEY #change for real secret

def getAuth():
    return auth

