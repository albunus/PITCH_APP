from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login import login_user,login_required,logout_user
from .forms import RegForm,LoginForm
from ..models import User
from .. import db
from ..emails import mail_message

@auth.route('/login', methods = ['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email = form.email.data).first()
    if user != None and user.verify_password(form.password.data):
      login_user(user,form.remember.data)
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or Password')
  return render_template('auth/login.html', loginform = form)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for("main.index"))

@auth.route('/register', methods = ["GET","POST"])
def register():
  form = RegForm()
  if form.validate_on_submit():
    user = User(email = form.email.data, username = form.username.data, password = form.password.data)
    db.session.add(user)
    db.session.commit()
    mail_message("Welcome to the Pitch","email/welcome_user",user.email,user=user)
    return redirect(url_for('auth.login'))
    title = "New Account"
  return render_template('auth/register.html', r_form = form)