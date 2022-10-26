from unicodedata import category
from flask import Flask, render_template
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app)


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)  # returns a client


@app.route("/")
def home():
    subjects = ["words", "astronomy", "animal", "professors"]
    return render_template("home.html", categories=subjects)


@app.route("/home/<category>", methods=["GET"])
def getCategoryData(category):
    client = connect()
    pool = client.get_database("pool")
    mango_c = pool.mango  # mango collection
    query = mango_c.find_one({"category": category})
    client.close()
    return {"category": query["category"], "objects": query["objects"]}


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=False)
