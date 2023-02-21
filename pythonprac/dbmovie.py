from pymongo import MongoClient
import certifi
import requests

ca = certifi.where()

# mongoDB에서 connect -> connect your application -> driver: python 3.6 or later -> copy
client = MongoClient(
    'mongodb+srv://sparta:test@cluster0.gsiejtz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

db.movies.update_one({'title': '가버나움'}, {'$set': {'point': 0}})

print(db.movies.find_one({'title': '가버나움'}))