from flask import Flask
from flask_cors import CORS
import pymongo


app = Flask(__name__)
CORS(app)


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url) # returns a client 
# To insert a single document into the database,
# insert_one() function is used
@app.route("/")
def home():
    return "Mango!!!!"

@app.route("/subject/<subject>", methods=["GET"])
def getSubjectData(subject):
    pool =
    mango_c = pool.mango
    query = mango_c.find_one({"subject": subject})
    return {"subject": query["subject"], "topics": query["topics"]}


if __name__ == "__main__":
    app.run(debug=True)
