from flask import Flask, render_template, redirect, url_for, request, session
from formulaires import Connexion 
from pymongo import MongoClient
from formulaires import Connexion
from forms import RegisterForm
from config import Config

app = Flask(__name__)
url = "mongodb://localhost:27017"
client = MongoClient(url)

#app.config['SECRET_KEY'] = 'Secret'
app.config.from_object(Config)

@app.route("/")
def accueil():
    form = Connexion()
    
    return render_template("accueil.html", form = form)

db = client.blog
articles = db.article  # une collection article

@app.route("/", methods = ['GET','POST'])
def accueil():
    form = Connexion()

    return render_template("accueil.html", form = form , articles = articles.find())

@app.route('/article/<nom>')
def article(nom):
    return render_template("article.html", titre=nom)

@app.route('/register')
def register():
    form = RegisterForm()

    return render_template('register.html', form = form, title = 'Resister')