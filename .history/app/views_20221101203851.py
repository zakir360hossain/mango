from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
import pymongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "mango"
socketio = SocketIO(app, cors_allowed_origins="*")

numberOfClients = 0

connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)  # returns a client


@app.route("/")
def home():
    return "Mango!!!!"


def getCategoryData(category):
    pool = client.get_database("pool")
    mango_c = pool.mango  # mango collection
    query = mango_c.find_one({"category": category})
    return {"category": query["category"], "objects": query["objects"]}


@app.route("/home.html")
def get_home():
    return render_template("home.html")


@socketio.event
def arrive(msg):
    print(f"\n{msg}\n")
    emit("received", {"data": "next clue!"})


@socketio.on("connect")
def connect(msg):
    global numberOfClients 
    

    if numberOfClients >= 2 :
        data = getCategoryData("words")
        emit("startGame", data)


@socketio.on("message")
def message(msg):
    print(msg)
    emit("message", {"data": "welcome!"})


if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)
    client.close()
