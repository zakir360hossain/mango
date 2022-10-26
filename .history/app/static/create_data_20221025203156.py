# import json
import pymongo


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)


def createSubject(category):
    client = connect()
    pool = client.get_database("pool")
    words_c = pool.words
    word_sets = words_c.find({})
    words = word_sets[0]["words"] + word_sets[1]["words"]
    objects = []
    for word in words[:100]:
        topic = {"object": word["word"], "clue": word["definition"]}
        objects.append(topic)
    mango_c = pool.mango
    mango_c.insert_one({"category": category, "objects": objects})
    client.close()


if __name__ == "__main__":
    createSubject("words")
