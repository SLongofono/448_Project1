## @file __init__.py
# @author Stephen Longofono
# @brief Decouples app instantiation and configuration from use
#
# @details
#
# This module exists to decouple the Flask app object and its configuration
# from the views and other pieces of the project.  It should not be run directly;
# it will be called by 'run.py' when it has finished running its setup steps.
#

from flask import Flask

app = Flask(__name__)
app.config.from_object('config') #secret config settings file
from app import views
app.secret_key = app.config['SECRET_KEY']
