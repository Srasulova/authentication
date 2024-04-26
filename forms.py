from wtforms import Form, StringField, PasswordField, EmailField, validators

# Define WTForm for user registration
class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=20)])
    password = PasswordField('Password', [validators.Length(min=6)])
    email = EmailField('Email', [validators.Length(min=6, max=50), validators.Email()])
    first_name = StringField('First Name', [validators.Length(min=1, max=30)])
    last_name = StringField('Last Name', [validators.Length(min=1, max=30)])

# Define WTForm for user login
class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')
