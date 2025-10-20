from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(max=64)])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Registrar")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")
    submit = SubmitField("Login")
    

class CarForm(FlaskForm):
    make = StringField("Marca", validators=[DataRequired(), Length(max=80)])
    model = StringField("Modelo", validators=[DataRequired(), Length(max=80)])
    year = StringField("Año", validators=[DataRequired()])
    price = StringField("Precio", validators=[DataRequired()])
    submit = SubmitField("Guardar")
