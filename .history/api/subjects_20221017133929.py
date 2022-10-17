from flask import Flask
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app)


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)  # returns a client


@app.route("/")
def home():
    return "Mango!!!!"


@app.route("/category/<category>", methods=["GET"])
def getCategoryData(category):
    client = connect()
    pool = client.get_database("pool")
    mango_c = pool.mango  # mango collection
    query = mango_c.find_one({"category": category})
    client.close()
    return {"category": query["category"], "objects": query["objects"]}


if __name__ == "__main__":
    app.run(debug=False)

words['objects']