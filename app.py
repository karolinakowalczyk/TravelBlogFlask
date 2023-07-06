from flask import Flask
from views import site


app = Flask(__name__)
app.secret_key = 'secret'

app.register_blueprint(site, url_prefix="")


if __name__ == "__main__":
    app.run()
# @app.route('/')
# def hello():
#     return "Flask heroku app"