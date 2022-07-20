from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import Form, BooleanField, StringField, PasswordField, validators, EmailField, SubmitField

class Connexion(FlaskForm):
    login = EmailField("login")
    password = PasswordField("password")
    submit = SubmitField("Se connecter")

class RegistrationForm(Form):
    username = StringField('Nom:', [validators.Length(min=4, max=25)])
    email = StringField('Email:', [validators.Length(min=6, max=35)])
    password = PasswordField('Mot de passe:', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField("Créer votre compte")