# import json
import pymongo
import random


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)


def createSubject(category, objects):
    client = connect()
    pool = client.get_database("pool")
    # words_c = pool.words
    # word_sets = words_c.find({})
    # words = word_sets[0]["words"] + word_sets[1]["words"]
    # objects = []
    # for word in words:
    #     topic = {"object": word["word"], "clue": word["definition"]}
    #     objects.append(topic)
    # print(objects[0])
    mango_c = pool.mango
    mango_c.insert_one({"category": category, "objects": objects})
    client.close()

def createRandomObjects():
    numbers = []

    for i in range(25):
        numbers.append({'object': i+1, 'clue': i+1})
    return numbers


if __name__ == "__main__":
    createSubject('numbers', createRandomObjects())
    # createRandomObjects()
