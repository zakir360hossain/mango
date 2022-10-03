# import json
import pymongo


connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)

pool = client.get_database("pool")


def createSubject(subject):
    # words_c = pool.words
    # query = words_c.find()
    # words = query[0]["words"] + query[1]["words"]
    # print(words[0])
    mango = pool.mango
    mango_c.insert_one({"words": words})


if __name__ == "__main__":
    createWords()
