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
    

    def save_comment(self):
            db.session.add(self)
            db.session.commit()

    @classmethod
    def get_comments(cls,id):
            comments = Comments.query.filter_by(pitch_id=id).all()
            return comments

    def __repr__(self):
        return f'COMMENT  {self.comment}'    

class Quote:
    def __init__(self,author,id,quote):
        self.author = author
        self.id = id
        self.quote = quote           
