import discord
import os
import json
import api
import User

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    if not os.path.exists('knownUsers'):
        open('knownUsers', 'w').close()
    if not os.path.exists('users'):
        os.mkdir('users')
    if not os.path.exists('shared'):
        os.mkdir('shared')
    if not os.path.exists('sharedLists'):
        open('sharedLists', 'w').close()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().split()[0] == 'todo':
        name = str(message.author)
        with open('knownUsers', 'r') as knownUsers:
            if not name in knownUsers.read().splitlines():
                open('knownUsers', 'a').write(name + '\n')
                await message.channel.send('Hello new user! Add something to your todo with `todo add new todo item`')
            knownUsers.close()

        todo = 'users/' + name
        if not os.path.exists(todo):
            open(todo, 'w').close()
        user = User.User(todo, name)
        content = message.content.split()
        if len(content) <= 1: return
        if content[1].lower() in open('sharedLists', 'r').read().splitlines():
            user = User.User('shared/' + content[1].lower(), content[1].lower())
            name = content[1].lower()
            content.pop(1)
        if content[1] == 'list':
            msg = name + '\'s todo is:\n'
            for i in range(len(user.read())):
                msg += str(i + 1) + '. ' + str(user.read()[i])
            await message.channel.send(msg)

        if content[1] == 'add':
            if len(content) >= 3:
                if content[-1].isdigit():
                    todo = ''
                    for i in range(2, len(content ) - 1):
                        print(content[i])
                        todo += content[i] + ' '
                    user.add(todo, int(content[-1]) - 1)
                    return
            todo = ''
            for i in range(2, len(content)):
                print(content[i])
                todo += content[i] + ' '
            user.add(todo)
        if content[1] == 'rename':
            todo = ''
            for i in range(3, len(content)):
                print(content[i])
                todo += content[i] + ' '
            user.rename(int(content[2]) - 1, todo)
        if content[1] == 'move':
            user.move(int(content[2]) - 1, int(content[3]) - 1)

        if content[1] == 'remove':
            user.remove(int(content[2]) - 1)

        if content[1] == 'new':
            if content[2].lower() in open('sharedLists', 'r').read().splitlines():
                await message.channel.send('That TODO already exists')
                return
            else:
                with open('sharedLists', 'a') as f:
                    f.write(content[2] + '\n')
                open('shared/' + content[2], 'w').close

client.run(api.getKey())
