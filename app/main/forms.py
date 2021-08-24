from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField("Post Title", validators = [Required()])
    category = StringField("Which category are you submitting to?",validators=[Required()])
    post_content = TextAreaField('Post Content' )
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment= TextAreaField('Add a comment',validators = [Required()] )
    submit = SubmitField('Submit')

