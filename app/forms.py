# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField, SelectField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
	name        = StringField  (u'Name'      )
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])
	email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])


class Youtube(FlaskForm):
	youtube_link    = StringField  (u'Youtube',validators=[DataRequired()])
	youtube_type    = SelectField  ('Quality',default=None,choices = [],validate_choice=False)

class Voiceover(FlaskForm):
	voiceover_text    = TextAreaField  ('Text',validators=[DataRequired()],render_kw={"placeholder": "Enter your message... ", "rows": "4"})
	
	