from flask import Flask

app = Flask(__name__)
app.config.from_object('config') #secret config settings file
from app import views
app.secret_key = app.config['SECRET_KEY']
