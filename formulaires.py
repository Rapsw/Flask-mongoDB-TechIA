from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, PasswordField, EmailField, SubmitField

class Connexion(FlaskForm):
    login = EmailField("login")
    password = PasswordField("password")
    submit = SubmitField("Se connecter")

