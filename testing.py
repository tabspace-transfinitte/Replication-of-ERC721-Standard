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
    print(result['collName'])
    return result


from discord.ext import commands
import discord
import os
import subprocess
import os
import discord
import pandas as pd
from dotenv import load_dotenv
import requests
import shutil
import server 

result = server.test.result
print(result)

load_dotenv()
intents = discord.Intents.all()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='?',intents=intents)

@client.event
async def on_ready()

@client.event
async def on_message(message):
    ctx = await client.get_context(message)
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        pass
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            print(type(url))
            subprocess.call(["./nft.sh", name, collection,url])

client.run(TOKEN)