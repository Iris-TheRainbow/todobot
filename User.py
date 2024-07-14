class User():
    def __init__(self, todopath, name):
        self.path = todopath
        with open(self.path, 'r') as f:
            self.todo = f.read().splitlines()
            f.close()
        for i in range(len(self.todo)):
            if not self.todo[i].endswith('\n'):
                self.todo[i] += '\n'
        self.name = name

    def read(self):
        return self.todo

    def add(self, message, place = 0):
        message += '\n'
        if place != 0:
            self.todo.insert(place, message)
        else:
            self.todo.append(message)
        self.update()

    def move(self, initial, position):
        data = self.todo[initial]
        self.todo.pop(initial)
        self.todo.insert(position, data)
        self.update()

    def remove(self, position):
        self.todo.pop(position)
        self.update()

    def rename(self, position, newString):
        self.todo[position] = newString + '\n'
        self.update()

    def update(self):
        print(self.todo)
        with open(self.path, 'w') as f:
            f.writelines(self.todo)
            f.close()
