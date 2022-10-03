from flask import Flask
from flask_cors import CORS
import pymongo


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    
app = Flask(__name__)
CORS(app)

pool = client.get_database("pool")

# To insert a single document into the database,
# insert_one() function is used
@app.route("/")
def home():
    return "Mango!!!!"


@app.route("/subject/<subject>", methods=["GET"])
def getSubjectData(subject):
    mango_c = pool.mango
    query = mango_c.find_one({"subject": subject})
    return {"subject": query["subject"], "topics": query["topics"]}


if __name__ == "__main__":
    app.run(debug=True)
