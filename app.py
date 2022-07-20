from flask import Flask, render_template, redirect, url_for, request, session
from formulaires import Connexion, RegistrationForm
from pymongo import MongoClient
from wtforms import Form, BooleanField, StringField, validators, EmailField, SubmitField

app = Flask(__name__)
url = "mongodb://localhost:27017"
client = MongoClient(url)

app.config['SECRET_KEY'] = 'Secret'


db = client.blog
articles = db.article  # une collection article

@app.route("/", methods = ['GET','POST'])
def accueil():
    try:
        login = session["login"]
    except:
        login = None

    return render_template("accueil.html", articles = articles.find(), login=login)

@app.route('/article/<nom>')
def article(nom):
    return render_template("article.html", titre=nom)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    utilisateur = {"login" : "antoine.meresse@info", "password" : "azerty"}
    form = Connexion()
    if form.validate_on_submit():
        if form.data["login"] == utilisateur["login"] and form.data["password"] == utilisateur["password"]:
            session["login"] = utilisateur["login"]
            return redirect(url_for("acceuil"))
    return render_template("login.html", form=form)

#maj kamel

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
        



    
