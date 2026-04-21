import discord
import asyncio
import os
import json

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # needed to read messages

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # ignore your own bot
    if message.author == client.user:
        return

    # command to change time delay of counting
    if message.author.id == 647946543411757059 and message.content.startswith("!delay "):
        parts = message.content.split(" ", 1)
        value = int(parts[1])
        with open("count_time_delay.json", "w") as file:
            json.dump(value, f)
    
    # code to count with Baby Mario
    if message.author.id == 647946543411757059 or message.author.id == 1067461387242192896:
        with open("count_time_delay.json", "r") as file:
            time = json.load(file)
        await asyncio.sleep(time)
        num = int(message.content)
        num += 1
        num = str(num)
        await message.channel.send(num)

    

client.run(TOKEN)
