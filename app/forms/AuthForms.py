from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length,Optional

class RegistrationForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=5)])
    address = StringField("Address",validators=[Optional(),Length(max=255)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField('Login')

    