# import json
import pymongo


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)


def createSubject(subject, topics):
    client = connect()
    pool = client.get_database("pool")
    words_c = pool.words
    word_sets = words_c.find()
    words = word_sets["words"] + word_sets["words"]
    print(words[0])

    # mango_c = pool.mango
    # mango_c.insert_one({"subject": subject, "topics": topics})


if __name__ == "__main__":
    createSubject("words")