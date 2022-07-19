from flask import Flask, render_template, redirect, url_for, request, session
from formulaires import Connexion 
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Secret'

@app.route("/")
def accueil():
    form = Connexion()
    
    return render_template("accueil.html", form = form)


@app.route('/article/<nom>')
def article(nom):
    return render_template("article.html", titre=nom)
