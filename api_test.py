from flask import Flask, jsonify
from threading import Thread


app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


@app.route('/testadd', methods=['GET'])
def add():
  return jsonify({"2 + 2": 2 + 2})


def run():
  app.run(host='0.0.0.0', port=7000)


t = Thread(target=run)
t.start()