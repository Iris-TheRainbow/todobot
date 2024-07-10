
from discord.message import Message


class user():
    def __init__(self, todopath, name):
        self.path = todopath
        with open(self.path, 'r') as f:
            self.todo = f.read().splitlines()
            f.close()
        self.name = name

    def add(self, message, place = 0):
        message += '\n'
        if place != 0:
            self.todo.insert(place, message)
        else:
            self.todo.append(message)

    def move(self, initial, position):
        self.todo.insert(position, self.todo[initial])
        self.update()

    def update(self):
        with open(self.path, 'r') as f:
            self.todo = f.read().splitlines()
            f.close()
