import asyncio
from config import config
import discord
import json
import os
import psycopg2
import random
import requests


client = discord.Client()

def connect():
    ''' Connect to the PostgreSQL database server'''
    conn = None
    try:
        # read connection parameters
        params = config()
        
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        quote = get_quote(cur)
        formated_quote = '"{0}" -{1}'.format(quote[0][1], quote[0][0])
        
        return formated_quote

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def get_quote(cur):
    cur.execute(
    ''' 
    SELECT authors.name, quotes.quote 
    FROM authors
    JOIN quotes
    ON authors.author_id = quotes.author_id
    WHERE quote_id = 32;
    ''')
    result = cur.fetchall()
    return result


async def send_quote():
    await client.wait_until_ready()
    channel = client.get_channel(id = 936051467985510410)
    await channel.send(connect())
    exit()


#To register an event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.loop.create_task(send_quote())
client.run(os.getenv('TOKEN'))
