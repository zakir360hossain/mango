from flask import Flask
from flask_cors import CORS
import pymongo
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)


def connect():
    connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
    return pymongo.MongoClient(connection_url)  # returns a client


# Handler for a message recieved over 'connect' channel
@socketio.on("connect")
def test_connect():
    emit("after connect", {"data": "Lets dance"})

@socketio.on('Slider value changed')
def value_changed(message):
    emit('update value', message, broadcast=True)

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
    socketio.run(app, allow_unsafe_werkzeug=True)
