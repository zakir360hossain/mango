from flask import Flask
from flask_cors import CORS
import pymongo
import os

url = os.environ('i')

app = Flask(__name__)
CORS(app)


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)  # returns a client

@app.route("/")
def home():
    return "Mango!!!!"


@app.route("/subject/<subject>", methods=["GET"])
def getSubjectData(subject):
    client = connect()
    pool = client.get_database("pool")
    mango_c = pool.mango
    query = mango_c.find_one({"subject": subject})
    client.close()
    return {"subject": query["subject"], "topics": query["topics"]}


if __name__ == "__main__":
    app.run(debug=True)
