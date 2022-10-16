
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


load_dotenv()
intents = discord.Intents.all()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='?',intents=intents)

name = 0
collection = 0

@client.event
async def on_ready():
    f = open("sample.txt","r")
    string = f.readlines()
    print(string)
    x = string[0]
    string = x.split()
    global name 
    name = string[1]
    global collection 
    collection = string[0]


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
            subprocess.call(["./collection.sh", collection])
            subprocess.call(["./nft.sh", name, collection,url]) 

client.run(TOKEN)