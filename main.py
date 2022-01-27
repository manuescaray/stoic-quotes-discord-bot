import discord
import os
from datetime import datetime
import json
import requests
import asyncio


client = discord.Client()


async def background_task():
    await client.wait_until_ready()
    target_date = "22:15"
    channel = client.get_channel(id = 936051467985510410)
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == target_date:
            await channel.send("Arigato")
        
        await asyncio.sleep(30)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = '"{}" —{}'.format(json_data[0]['q'], json_data[0]['a'])
    return quote


#To register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = client.get_channel(id = 936051467985510410) 
    if message.content.startswith("inspire"):
        quote = get_quote()
        await channel.send(quote)


client.loop.create_task(background_task())
client.run(os.getenv('TOKEN'))
