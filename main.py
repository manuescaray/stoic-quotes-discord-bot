import asyncio
import discord
import os
import json
import random
import requests



client = discord.Client()


async def background_task():
    await client.wait_until_ready()
    channel = client.get_channel(id = 936051467985510410)
    await channel.send(get_quote())
    exit()


def random_author()
    authors = {0: 'marcus-aurelius', 1: 'epictetus', 2: 'seneca'}


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = '"{}" —{}'.format(json_data[0]['q'], json_data[0]['a'])
    return quote


#To register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.loop.create_task(background_task())
client.run(os.getenv('TOKEN'))
