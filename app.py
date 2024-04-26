"""Flask app for Authentication app"""
from flask import Flask, render_template, redirect, flash, request, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import User, connect_db, db
from forms import RegistrationForm, LoginForm



app = Flask(__name__)

app.config['SECRET_KEY'] = "abcdef"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Milagros@localhost/authorized_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

with app.app_context():
   connect_db(app)
   db.create_all()


@app.route('/')
def show_home_page():
   return redirect(url_for('register_page'))

@app.route('/register', methods=['GET', 'POST'])
def register_page():
   form = RegistrationForm()

   if form.validate_on_submit():
      username = form.username.data
      password = form.password.data
      email = form.email.data
      first_name = form.first_name.data
      last_name = form.last_name.data

      # Check if the username already exists
      if User.query.filter(username = username):
         flash("User already exists. Choose another username!")
         return redirect(url_for('register_page'))
      
      new_user = User(username, password, email, first_name, last_name)
      db.session.add(new_user)
      db.session.commit()

      flash("User created successfully! Redirecting to the login page")
      return redirect(url_for('login_page'))
   
   return render_template("register.html", form = form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
   form = LoginForm()

   if form.validate_on_submit():
      username = form.username.data
      password = form.password.data

      user = User.authenticate(username, password)

      if user:
         session["username"] = username
         flash("Login is successfull!", "success")
         return redirect(url_for('secret_page'))
      
      flash("Invalid username or password. Please try again", "danger")

   return render_template("login.html", form = form)


@app.route("/secret")
def secret_page():
   if 'username' not in session:
      flash("You need to login first!", "warning")
      return redirect(url_for('login_page'))
   
   return render_template("secret.html")
    