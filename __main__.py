import discord
import os
import json
import api

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    if not os.path.exists('knownUsers'):
        open('knownUsers', 'w').close()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('todo'):
        user = str(message.author)
        with open('knownUsers', 'r') as knownUsers:
            if not user in knownUsers.read().splitlines():
                open('knownUsers', 'a').write(user + '\n')
                await message.channel.send('First time user!')
            knownUsers.close()

        if not os.path.exists('users/' + user):
            open('users/' + user, 'w').close()

client.run(api.getKey())
