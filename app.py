from flask import Flask, render_template, redirect, url_for, request, session
from pymongo import MongoClient
from formulaires import Connexion

app = Flask(__name__)
url = "mongodb://localhost:27017"
client = MongoClient(url)

db = client.blog
articles = db.article  # une collection article

@app.route("/", methods = ['GET','POST'])
def accueil():
    form = Connexion()

    return render_template("accueil.html", form = form , articles = articles.find())

@app.route('/article/<nom>')
def article(nom):
    return render_template("article.html", titre=nom)
