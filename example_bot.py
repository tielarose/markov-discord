# This example requires the 'message_content' intent.

import discord
import os
from markov import make_chains, make_text

green_eggs = open("green-eggs.txt").read()

markov_message = make_text(make_chains((green_eggs)))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Give me a markov!"):
        await message.channel.send(markov_message)


client.run(os.environ["DISCORD_TOKEN"])
