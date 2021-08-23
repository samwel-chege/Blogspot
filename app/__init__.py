from flask import Flask
from config import DevConfig

#Initializing the application
app = Flask(__name__)


app.config.from_object(DevConfig)
from app import views