from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,length,Optional


class BlogForm(FlaskForm):
    title = StringField("title",validators=[DataRequired(),length(max=100)])
    description = StringField('description',validators=[Optional(),length(max=255)])
