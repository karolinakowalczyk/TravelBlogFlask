from flask import Flask
from flask_jwt_extended import JWTManager
from src.config import JWT_KEY


app = Flask(__name__)
app.config["JWT_TOKEN_LOCATION"] = [
    "headers", "cookies", "json", "query_string"]
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_SECRET_KEY"] = JWT_KEY

jwt = JWTManager(app)
