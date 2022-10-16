import json, os, signal, time
from flask import Flask, render_template, request, jsonify
import jyserver.Flask as jsf
import subprocess

app = Flask(__name__)

@jsf.use(app)
class App:
    def __init__(self):
        pass

@app.route("/")
def my_home():
    return App.render(render_template('index.html'))

@app.route("/create")
def my_create():
    return App.render(render_template('create.html'))

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    result = json.loads(output)
    file = open('sample.txt', 'w')
    file.write(result['collName'] + " " + result['nftName'])
    file.close()
    print(result['collName'])
    return result

