from distutils.log import debug
from socket import socket
from flask import request
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
import pymongo
import random
from numpy import random
import numpy as np


app = Flask(__name__)
app.config["SECRET_KEY"] = "mango"
socketio = SocketIO(app, cors_allowed_origins="*")

numberOfClients = 0

numberOfClientsClicked = 0

setOfWords = []

# setOfAvailableWords=[]

currentClueObject = None

numberOfPlayersReady = 0

players = []

connection_url = "mongodb+srv://zakir:mongo123@cluster0.abqkq.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)  # returns a client


@app.route("/")
def home():
    return "Mango!!!!"


def getCategoryData(category):
    pool = client.get_database("pool")
    mango_c = pool.mango  # mango collection
    query = mango_c.find_one({"category": category})
    response = {"category": query["category"], "objects": query["objects"]}
    global setOfWords
    for _ in range(9):
        object_clue = random.choice(response["objects"])
        while setOfWords.count(object_clue) > 0:
            object_clue = random.choice(response["objects"])
        # object_clue =response["objects"][Math.floor(Math.random() * (l - 0 + 1)) + 0]
        setOfWords.append(object_clue)
    global setOfAvailableWords
    global currentClueObject
    setOfAvailableWords = setOfWords
    currentClueObject = random.choice(setOfWords)


def setNewClue():
    global currentClueObject
    global setOfAvailableWords
    currentClueObject = random.choice(setOfAvailableWords)
    setOfAvailableWords.remove(currentClueObject)


@socketio.on("Timer Up")
def timerUp():
    setNewClue()
    global currentClueObject
    socketio.emit("newClue", currentClueObject)
    numberOfClientsClicked = 0


@socketio.on("clicked")
def clientClicked():
    global numberOfClientsClicked
    numberOfClientsClicked += 1
    global numberOfClients
    if numberOfClientsClicked == numberOfClients:
        setNewClue()
        global currentClueObject
        socketio.emit("newClue", currentClueObject)
        numberOfClientsClicked = 0


@socketio.on("Blackout")
def blackout(currentUser):
    socketio.emit("endGame", currentUser)


@socketio.on("playerReady")
def playerReady(currentUser):
    global numberOfPlayersReady
    players.append(currentUser)
    numberOfPlayersReady += 1
    global numberOfClients
    if len(players) == 2:
        socketio.emit("startGame", broadcast=True)


@app.route("/home.html")
def get_home():
    return render_template("home.html")


def shuffle(array):
    n = len(array) - 1
    for _ in range(n):
        random_index = random.randint(0, n)
        temp = array.pop(random_index)
        array.append(temp)


@socketio.on("checkName")
def checkDuplicate(currentUser):
    print(f"current user {currentUser}, players: {players}")
    message = currentUser in players
    emit("duplicateName", message)


@socketio.on("connect")
def connect():
    global numberOfClients

    numberOfClients += 1
    # need to increment when we submit a username, not when we connect

    if numberOfClients == 1:
        getCategoryData("numbers")

    global setOfWords

    wordsCopyToShuffle = setOfWords

    shuffle(wordsCopyToShuffle)
    print(wordsCopyToShuffle)

    global currentClueObject

    socketio.emit("newPlayer", numberOfClients, broadcast=True)

    socketio.emit("transferData", data=(wordsCopyToShuffle, currentClueObject))
    # if numberOfClients==2:
    #     socketio.emit('startGame',broadcast=True)


@socketio.on("disconnect")
def disconnect():
    global numberOfClients
    numberOfClients -= 1


@app.route("/result.html")
def have_Won():
    return render_template("result.html")


if __name__ == "__main__":
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
    client.close()
