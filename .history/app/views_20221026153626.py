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
host_id = None


@app.route("/")
def home():
    subjects = ["words", "astronomy", "animal", "professors"]
    return render_template("home.html", categories=subjects)


@app.route("/home/<category>", methods=["GET"])
def game(category):
    # pool = client.get_database("pool")
    # mango_c = pool.mango  # mango collection
    # query = mango_c.find_one({"category": category})
    # whole_set = query["objects"]
    # global current_set
    # sampled = random.sample(whole_set, 16)
    return render_template("decide.html")


@app.route("/home/hostDetail", methods=["GET"])
def host():
    return render_template("hostDetail.html")


@app.route("/home/playerDetail", methods=["GET"])
def player():
    return render_template("playerDetail.html")
@app.route("/home/playerDetail", methods=["GET"])
def player():
    return render_template("playerDetail.html")


@socketio.on("message")
def handleMessage(message):
    print(f"Message: {message}")
    send(message, broadcast=True)


@socketio.event
def clicked(message):
    emit(
        "clue_response",
        {"next": current_set[random.randint(1, 100)]},
        broadcast=True,
    )


@socketio.event
def create(data):
    global host_id
    host_id = data["game_id"]
    emit("open_door", {data}, broadcast=True)


@socketio.event
def join(data):
    player_id = data["game_id"]
    if id == player_id:
        emit("open_door", {data}, broadcast=True)
    else:
        emit("rejected", {data: "Invalid Id"})


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    socketio.run(app, allow_unsafe_werkzeug=True)
    client.close()
