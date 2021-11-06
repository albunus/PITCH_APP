from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class PitchForm(FlaskForm):
  content = TextAreaField('New Pitch')
  submit = SubmitField('Submit')


class CommentForm(FlaskForm):
  body = TextAreaField('New Comment')
  submit = SubmitField('Submit')