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

