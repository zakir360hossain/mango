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
    print(words[0])
    topics = []
    for word in words:
        topic = {"object": word["word"], "clue": word["definition"]}
        topics.append(topic)
    print(topics[0])

    # mango_c = pool.mango
    # mango_c.insert_one({"subject": subject, "topics": topics})


if __name__ == "__main__":
    createSubject("words")
