from wtforms import StringField, PasswordField, EmailField, validators
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

# Define WTForm for user registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), validators.Length(min=4, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), validators.Length(min=6)])
    email = EmailField('Email', validators=[InputRequired(), validators.Length(min=6, max=50), validators.Email()])
    first_name = StringField('First Name', validators=[InputRequired(), validators.Length(min=1, max=30)])
    last_name = StringField('Last Name', validators=[InputRequired(), validators.Length(min=1, max=30)])

# Define WTForm for user login
class LoginForm(FlaskForm):
    username = StringField('Username',  validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
