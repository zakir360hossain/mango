from flask import Flask, jsonify
from threading import Thread
import numpy as np



app = Flask('')

words = ["blasphemy", "monstrous", "gargantuan", "cyclone"]
definitions = ["the act or offense of speaking sacrilegiously about God or sacred things; profane talk.", "having the ugly or frightening appearance of a monster.", "enormous.", "a system of winds rotating inward to an area of low atmospheric pressure, with a counterclockwise (northern hemisphere) or clockwise (southern hemisphere) circulation; a depression." ]
currentIndex = 0

@app.route('/')
def home():
  return "I'm alive"


#uses GET by default
@app.route('/testadd')
def add():
  return jsonify({"2 + 2": 2 + 2})

@app.route('/clue')
def retClue():
  index = np.random.randint(0, len(words)-1)
  currentIndex = index
  clue = definitions[index]
  return jsonify(definitions[index])

@app.route('/answer')
def retAnswer():
  return jsonify(words[currentIndex])





def run():
  #app.run(host='0.0.0.0', port=7000)
  app.run()

if __name__ == '__main__':
  app.run()


t = Thread(target=run)
t.start()
