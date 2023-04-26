
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, validators


class AddPostForm(FlaskForm):
    title = StringField(
        'Title: ', [validators.InputRequired(), validators.Length(min=1, max=35)])
    author = StringField(
        'Author: ', [validators.InputRequired(), validators.Length(min=1, max=35)])
    images = FileField('Image', validators=[
                       FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
