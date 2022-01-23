#HIBOT07 Python Discord Bot
#Licensed under MIT License
#Do not reuse without permission

#Import libraries

import discord
import os
import requests
import json
import math

#vars
client = discord.Client()
token = os.environ['TOKEN']


#Console logs a ready message when the bot is online
@client.event
async def on_ready():
  print("We have logged in as {0.user}!".format(client))

#Commands
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("!hello"):
    await message.channel.send("Hello World!")

  if message.content.startswith("!inspire"):
    quote = getQuote()
    await message.channel.send(quote)

  if message.content.startswith('!help'):
        embedVar = discord.Embed(title="Help Menu", color=0x00ff00)
        embedVar.add_field(name="!hello", value="States 'Hello World'", inline=False)
        embedVar.add_field(name="!inspire", value="Sends a random inspirational quote", inline=False)
        embedVar.add_field(name="!about", value="States information about the bot", inline=False)
        await message.channel.send(embed=embedVar)

  if message.content.startswith('!about'):
    await message.channel.send("This bot was created by HiBad07!")

  if message.content.startswith('!ping'):
    ping = {client.latency} * 100
    await message.channel.send(ping)

#def truncate(number, digits) -> float:
#    stepper = 10.0 ** digits
#    return math.trunc(stepper * number) / stepper



#Quote function
def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

client.run(token)