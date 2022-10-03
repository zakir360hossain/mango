# import json
import pymongo



def 

def createSubject(subject, topics):
    # words_c = pool.words
    # query = words_c.find()
    # words = query[0]["words"] + query[1]["words"]
    # print(words[0])
    mango_c = pool.mango
    mango_c.insert_one({f"{subject}": topics})


if __name__ == "__main__":
    print("No functions called!")
