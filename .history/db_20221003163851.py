# import json
import pymongo


connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)

pool = client.get_database("pool")

def createWords():
    collection = pool[subject]
    query = collection.find()
    return {"subject": query[0]["words"]}