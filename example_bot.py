# This example requires the 'message_content' intent.

import discord
import os

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

    if message.content.startswith("How are you?"):
        await message.channel.send(
            "I was born 10 minutes ago and so far, life is...meh"
        )


client.run(os.environ["DISCORD_TOKEN"])
