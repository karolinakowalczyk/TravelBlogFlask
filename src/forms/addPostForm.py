from wtforms import Form, StringField, PasswordField, validators


class AddPostForm(Form):
    title = StringField(
        'Title: ', [validators.InputRequired(), validators.Length(min=1, max=35)])
    author = StringField(
        'Author: ', [validators.InputRequired(), validators.Length(min=1, max=35)])
