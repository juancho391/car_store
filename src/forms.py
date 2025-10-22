from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Optional


# LoginForm: holds credentials for authentication and a remember flag
class LoginForm(FlaskForm):
    # user's email used as username
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=256)])
    # plaintext password input (will be checked against hash in the model)
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    # keep session persistent
    remember_me = BooleanField('Remember me')
    # submit control for the form
    submit = SubmitField('Login')


# SignupForm: collects name, email and password for new user registration
class SignupForm(FlaskForm):
    # display name of the user
    name = StringField('Name', validators=[DataRequired(), Length(max=80)])
    # unique email address used to login
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=256)])
    # password with confirmation
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=128)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # submit control
    submit = SubmitField('Sign up')


# CarForm: used both for creating and updating car records
class CarForm(FlaskForm):
    # vehicle brand (make)
    make = StringField('Make', validators=[DataRequired(), Length(max=80)])
    # vehicle model name
    model = StringField('Model', validators=[DataRequired(), Length(max=80)])
    # production year, constrained to a reasonable range
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1900, max=2100)])
    # price as float
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    # optional image upload (handled in the view; validator Optional allows empty)
    image = FileField('Image', validators=[Optional()])
    # submit control for save/update
    submit = SubmitField('Save')
