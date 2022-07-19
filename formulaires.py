from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

class Connexion(FlaskForm):
    login = EmailField("login")
    password = PasswordField("password")
    password = PasswordField("password")

class RegisterForm(FlaskForm)
    email = StringField("Email", validators=[])
    submit = SubmitField("S'inscrire")


