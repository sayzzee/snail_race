class Snail:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.sleeping = False

    def __repr__(self):
        return (f'{self.name}')

    def move(self, steps):
        self.position += steps

    def push(self, steps):
        self.position += steps

    def sleep(self):
        self.sleeping = True

    def wakeup(self):
        self.sleeping = False