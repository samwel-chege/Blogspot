from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from . import main
from .. models import  User,Comments
# from .forms import CategoryForm, UpdateProfile,PitchForm,CommentForm
from .. import db,photos


@main.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''
    title = 'qoute_blogspot'
    return render_template('index.html',title = title)