from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp
from wtforms import ValidationError

from flask_login import current_user
from src.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForms(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=3, max=50)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=3, max=20), EqualTo('password',message = "Passwords must match")])
    submit = SubmitField('Sign Up')

    def checkEmail(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exists')
    
    def checkUsername(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists')

# TODO - add a form for changing password