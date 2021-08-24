from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model) :
    __tablename__ = 'users' 

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments = db.relationship('Comments', backref = 'author',lazy ="dynamic")
    pass_secure = db.Column(db.String(255))

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user(cls,id):
        user = User.query.filter_by(id=id).order_by(User.id.desc())  
        return user  

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')   

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)        

    def __repr__(self):
        return f'USER {self.username}' 



class Comments(db.Model):
    __tablename__ = 'comments' 
    id = db.Column(db.Integer,primary_key = True)  
    comment = db.Column(db.String(255))  
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    

    def save_comment(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_comments(cls,id):
            comments = Comments.query.filter_by(pitch_id=id).all()
            return comments

    def __repr__(self):
        return f'COMMENT  {self.comment}'  

class Post(db.Model):
        __tablename__ = 'posts'
        id = db.Column(db.Integer,primary_key = True)
        title = db.Column(db.String())
        post_content = db.Column(db.String())
        short_description = db.Column(db.String())
        posted = db.Column(db.DateTime,default=datetime.utcnow)
        post_pic_path = db.Column(db.String())
        author_id = db.Column(db.Integer,db.ForeignKey("users.id"))
        comments = db.relationship("Comments", backref ='user', lazy = "dynamic")

        def save_post(self):
                db.session.add(self)
                db.session.commit()

        @classmethod
        def get_user_post(cls,id):
                user_posts = Post.query.filter_by(author_id = id).order_by(Post.posted.desc())
                return user_posts

        @classmethod
        def get_posts(cls):
                all_posts = Post.query.order_by(Post.posted.desc())
                return all_posts

        @classmethod
        def get_post(cls,id):
                post= Post.query.filter_by(id = id).first() 
                return post

        def __repr__(self):
                return f"POST {self.title}"

class Quote:
    def __init__(self,author,id,quote):
        self.author = author
        self.id = id
        self.quote = quote           
