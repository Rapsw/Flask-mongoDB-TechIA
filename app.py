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
users = db.user

@app.route("/", methods = ['GET','POST'])
def accueil():
    try:
        login = session["login"]
    except:
        login = None

    return render_template("accueil.html", articles = articles.find(), login=login)

@app.route('/article/<nom>')
def article(nom):
    article_selectionne = articles.find_one({"titre" : nom})
    return render_template("article.html", article=article_selectionne)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = Connexion()
    if form.validate_on_submit():
        user = users.find_one({"nom" : form.data["username"],"mdp" : form.data["password"]})
        if user is not None:
            session["username"] = form.data["username"]
            return redirect(url_for("accueil"))
        else:
            return redirect(url_for("register"))
    return render_template("login.html", form=form)

#maj kamel

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = {
            "nom" : form.data["username"],
            "mdp" : form.data["password"],
            "mail" : form.data["email"],
        }
        users.insert_one(new_user)
        return redirect(url_for("login"))
    return render_template('register.html', form=form)
        



    
