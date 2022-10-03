# import json
import pymongo


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)


def createSubject(subject):
    pool = connect().get_database("pool")
    words_c = pool.words
    query = words_c.find()
    words = query[0]["words"] + query[1]["words"]
    print(words[0])
    pool = connect().get_database("pool")
    mango_c = pool.mango
    mango_c.insert_one({"subject": subject, "topics": words})


if __name__ == "__main__":
    createSubject("words")
