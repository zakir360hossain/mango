# import json
import pymongo


connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)

pool = client.get_database("pool")

def createWords():
    words_c = pool.words
    query = words_c.find()
    words = query[0]["words"] + query[1]["words"]
    print(words[0])
    mango_c = pool.mango
    mango_c.insert_one{"subject": words, "topics": words}



if __name__ == "__main__":
    createWords()
