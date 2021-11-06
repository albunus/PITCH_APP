from flask import render_template, redirect, url_for, abort, flash, request
from . import main
from flask_login import login_required, current_user

from app.models import User, Post, Comment



@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    print(posts)
    return render_template('index.html', posts=posts)