from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Pitch(db.Model):
  __tablename__ = 'pitches'
  id = db.Column(db.Integer,primary_key= True)
  content = db.Column(db.String(255))
  date_posted =db.Column(db.DateTime,default = datetime.utcnow)
  category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  comments = db.relationship("Comments", backref = 'pitch', lazy ='dynamic')

  def save_pitch(self):
    db.session.add(self)
    db.session.commit()
  @classmethod
  def get_pitch(cls,id):
    pitches = Pitch.query.order_by(Pitch.date_posted.desc()).filter_by(category_id =id)
    return pitches
  @classmethod
  def get_all_pitches(cls):
    all_pitches = Pitch.query.all()
    return all_pitches

class Category(db.Model):
  __tablename__ = 'categories'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(140))
  pitches = db.relationship('Pitch', backref='category',lazy='dynamic')

  @classmethod
  def get_categories(cls):
    categories = Category.query.all()
    return categories

class Comments(db.Model):
  __tablename__ = "comments"
  id = db.Column(db.Integer,primary_key = True)
  body = db.Column(db.String(255))
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))  
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comment(self,id):
    comments = Comments.query.filter_by(pitch_id =id).all()
    return comments

class User(UserMixin,db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer,primary_key= True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True, index = True)
  password_hash = db.Column(db.String(255))
  pitches = db.relationship("Pitch", backref = 'user', lazy = 'dynamic')
  comments = db.relationship("Comments", backref = 'user', lazy = 'dynamic')



@property
def password(self):
    raise AttributeError("You cannot read the password attribute")
@password.setter
def password(self,password):
    self.password_hash = generate_password_hash(password)

def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

