from pymongo import MongoClient
from datetime import datetime 

url = "mongodb://localhost:27017"
client = MongoClient(url)

db = client.blog
 
article = db.article  # une collection 

article.drop() #nettoyer la base de données 


article.insert_one (
    { "titre" : "TITRE 1", "résumé" : "résumé 1" , "date" :str(datetime.now()), "texte" : "Lorem " , 
    "commentaires":   [ {"user": "De Niro", "texte": "test commentaire"}]}  
   )

article.insert_one (
 {"titre" : "ARTICLE 2" , "résumé" : "résumé 3" , "date" :str(datetime.now()), "texte" : "test " } )

article.insert_one ( {"titre" : "ARTICLE 3" , "résumé" : "résumé 3" , "date" :str(datetime.now()), "texte" : "test 2  " } )


# afficher la base de données 
# afficher une collection
#curseur = article.find_one({"titre" : "ARTICLE2"})
curseur = article.find({})
print (curseur)

for article in curseur:
    print(article)

