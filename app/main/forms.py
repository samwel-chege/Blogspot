from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Email, Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField("Post Title", validators = [Required()])
    short_description = StringField("Give a short decription of your post",validators = [Required()])
    post_content = TextAreaField('Post Content' )
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment= TextAreaField('Add a comment',validators = [Required()] )
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField('Your Email Adress', validators=[Required(),Email()])
    submit = SubmitField('Subscribe')
