from flask import Flask
from config import config_options

def create_app(config_name):

#Initializing the application
    app = Flask(__name__)


    app.config.from_object(config_options[config_name])
    from app import views