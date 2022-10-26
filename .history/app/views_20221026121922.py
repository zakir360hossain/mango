import random
from flask import Flask, render_template
from flask_cors import CORS
import pymongo
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "mangoo"
CORS(app)
socketio = SocketIO(app)


connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)  # returns a client

current_set = []
@app.route("/")
def home():
    subjects = ["words", "astronomy", "animal", "professors"]
    return render_template("home.html", categories=subjects)


@app.route("/home/<category>", methods=["GET"])
def game(category):
    pool = client.get_database("pool")
    mango_c = pool.mango  # mango collection
    query = mango_c.find_one({"category": category})
    whole_set = query["objects"]
    global current_set
    current_set = whole_set
    sampled = random.sample(whole_set, 25)
    return render_template("game.html", data=sampled, current=whole_set[0])


@socketio.on("message")
def handleMessage(message):
    print(f"Message: {message}")
    send(message, broadcast=True)


@socketio.event
def clicked(message):
    print(message)
    emit("clue_response", {"next_clue": }, broadcast=True)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    socketio.run(app, allow_unsafe_werkzeug=True)
    client.close()
