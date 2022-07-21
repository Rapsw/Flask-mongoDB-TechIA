from collections import UserString
from pymongo import MongoClient
from datetime import datetime 

url = "mongodb://localhost:27017"
client = MongoClient(url)

db = client.blog
 
article = db.article  # une collection 


article.drop() #nettoyer la base de données 


article.insert_one (
    { "titre" : "Projet Wa-Tor", 
    "résumé" : "A l'aide de vos connaissances en Python et au logiciel Processing, vous simulerez  la vie et les interactions entre une population de proies et de prédateurs dans une mer de forme torique (forme de donuts)" ,
     "date" :str(datetime.now()), 
     "texte" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum " , 
    "commentaires":   [ {"user": "De Niro", "texte": "test commentaire"}]}  
   )

article.insert_one (
 {"titre" : "Logiciel d'Histoires Participatif" , 
 "résumé" : "Le site communautaire Reddit, habitué des défis collaboratifs, a décidé de lancer une nouvelle expérimentation.Cette fois-ci, ils souhaitent regarder ce qui se passe quand on laisse de nombreux internautes écrire une histoire, tous ensemble." ,
  "date" :str(datetime.now()), 
  "texte" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum " } )

article.insert_one ( {"titre" : "Réalisation Blog avec Flask et MongoDB" ,
    "résumé" : "Vous souhaitez réaliser un blog afin de montrer ce que vous avez vu en formation, mais aussi pour partager vos veilles quotidiennes sur le sujet de l'IA, de la data et du développement en général." , 
    "date" :str(datetime.now()), 
    "texte" : "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum " } )

admin = db.admin
admin.insert_one({"username": "admin", "email": " admin@gmail.com" , "password" : "mdp"})


users =db.users # collection users

users.drop()

user1={"name":"name1","passeword":"passeword1","email":"email1"}
user2={"name":"name2","passeword":"passeword2","email":"email2"}
user3={"name":"name3","passeword":"passeword3","email":"email3"}
user4={"name":"name4","passeword":"passeword4","email":"email4"}
user5={"name":"name5","passeword":"passeword5","email":"email5"}

users.insert_many([user1,user2,user3,user4,user5])



# afficher la base de données 
# afficher une collection
#curseur = article.find_one({"titre" : "ARTICLE2"})
curseur = users.find({})
print (curseur)

for article in curseur:
    print(article)

