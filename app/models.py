from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


class Category(db.Model):  # category table
    _tablename_ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    post = db.relationship('Post', backref='category', lazy='dynamic')

    # save category

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Category {self.name}'


class Post(db.Model):  # post table
    _tablename_ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # save post

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def _repr_(self):
        return f'Post {self.title}'


class User(UserMixin, db.Model):  # user table
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # comments = db.relationship('Comment', backref='author', lazy='dynamic')

    # save user

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    # generate password hash

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # check password

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # login manager

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def _repr_(self):
        return f'User {self.username}'

# comment table
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment {self.content}'