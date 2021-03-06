import datetime as date
from pymongo import MongoClient

conn = MongoClient('localhost', 27017) # make connection with database (host and port)

# just one instance of MongoDB can support multiple databases
db = conn.cadastrodb # database cadastrodb

 # a collection its a group of documents stored in MongoDB
collection = db.cadastrodb # collections in DOC-DBMS (NoSQL) are like tables in RDBMS (SQL)

 # dicts
post1 = {
	'codigo':"ID-214436",
	'prod_nome':"Geladeira",
	'marcas':["brastemp", "electrolux", "consul"],
	'data_cadastro':date.datetime.utcnow()
}
post2 = {
	'codigo':"ID-357689", # fields in DOC-DBMS (NoSQL) are like columns in RDBMS (SQL)
	'prod_nome':"Televisor",
	'marcas':["lg", "panasonic", "sansung"],
	'data_cadastro':date.datetime.utcnow()
}

collection = db.posts
post_id = collection.insert_one(post1) # documents in DOC-DBMS (NoSQL) are like lines in RDBMS (SQL)
print(post_id.inserted_id)
post_id = collection.insert_one(post2).inserted_id
print(post_id)
print()
#db.collection.delete_many({})

for post in collection.find():
	print(post)
	collection.delete_one(post)
	print()

print()
print(db.name)
print(db.list_collection_names())
print()
