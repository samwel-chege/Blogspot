from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from . import main
from .. models import  MailList, User,Comments,Post
from .forms import SubscribeForm, UpdateProfile,PostForm,CommentForm
from .. import db,photos
from ..request import get_quotes,repeat_get_quotes

@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    view root page that returns the index page and its data
    '''
    title = 'qoute_blogspot'
    quote = get_quotes()
    quotes = repeat_get_quotes(10, get_quotes)
    all_posts =Post.get_posts()
    posts = all_posts.paginate(per_page = 6)
    form = SubscribeForm()

    if form.validate_on_submit():
        email = form.email.data
        new_email = MailList(email = email)

        db.session.add(new_email)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('index.html',title = title,posts = posts,quotes = quotes,subscribe_form = form)