import random

class Computer:
    def __init__(self, name):
        self.name = name
    def makemove(self, max):
        return random.randint(0, max)
    def getname(self):
        return self.name
