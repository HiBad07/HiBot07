#HIBOT07 Python Discord Bot
#Licensed under MIT License
#Do not reuse without permission

#Import libraries

import discord
import os
import requests
import json
import math
import random

#vars
client = discord.Client()
token = os.environ['TOKEN']
depressing_quotes = [
  "All alone! Whether you like it or not, alone is something you'll be quite a lot! - Dr Seuss",
  "Y'all smoke to enjoy it. I smoke to die. - Victor Rollin",
  "From the moment we are born, we begin to die. - BRB",
  "She can paint a pretty picture but this story has a twist. The paintbrush is a razor and the canvas is her wrist.",
  "Why does no one love me, and why do I gain 30lbs per day - Discord Mod",
  "If she has big t*ts, she wont like my nits - BRB",
  "Just kill yourself",
  "Do it, jump off that bridge, no one wants you here you waste of space",
  "Scotsmen deserve a bullet in the skull"
  ""
]

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
        embedVar.add_field(name="!dquote", value="Sends a random depressing quote", inline=False)
        await message.channel.send(embed=embedVar)

  if message.content.startswith('!about'):
    await message.channel.send("This bot was created by HiBad07!")

  if message.content.startswith('!ping'):
    ping = float({client.latency}) * 100
    ping2 = float(ping)
    await message.channel.send(ping2)

  if message.content.startswith('!dquote'):
    random_index = random.randint(0,len(depressing_quotes)-1)
    await message.channel.send(depressing_quotes[random_index])


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