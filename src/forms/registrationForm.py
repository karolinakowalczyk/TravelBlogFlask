from wtforms import Form, StringField, PasswordField, validators


class RegistrationForm(Form):
    email = StringField(
        'Email: ', [validators.InputRequired(), validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message="Passwords aren't same")
    ])
    confirm = PasswordField('Repeat Password')
