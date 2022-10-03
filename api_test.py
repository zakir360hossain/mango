from flask import Flask, jsonify
from threading import Thread
import numpy as np



app = Flask('')

words = ["blasphemy", "monstrous", "gargantuan", "cyclone"]
definitions = ["the act or offense of speaking sacrilegiously about God or sacred things; profane talk.", "having the ugly or frightening appearance of a monster.", "enormous.", "a system of winds rotating inward to an area of low atmospheric pressure, with a counterclockwise (northern hemisphere) or clockwise (southern hemisphere) circulation; a depression." ]


@app.route('/')
def home():
  return "I'm alive"


@app.route('/testadd', methods=['GET'])
def add():
  return jsonify({"2 + 2": 2 + 2})

@app.route('/words', methods = ['GET'])
def retWord():
  index = np.random.randint(0, len(words)-1)
  word = words[index]
  return jsonify(word, definitions[index])



def run():
  app.run(host='0.0.0.0', port=7000)


t = Thread(target=run)
t.start()