from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, PasswordField, EmailField

class Connexion(FlaskForm):
    login = EmailField("login")
    password = PasswordField("password")
    password = PasswordField("password")
