import random
from flask import Flask, render_template
from flask_cors import CORS
import pymongo
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "mangoo"
CORS(app)
socketio = SocketIO(app)


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
    whole_set = random.sample(query["objects"], 100)
    sampled = random.sample(whole_set, 25)
    client.close()
    return render_template("game.html", data=sampled, all_data=whole_set)

@socketio.on('')
def handle
if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    socketio.run(app, allow_unsafe_werkzeug=True)
