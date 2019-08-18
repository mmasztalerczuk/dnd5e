from random import randint


class Dice:
    def __init__(self, size):
        self.size = size
        self.result = 0

    def roll(self):
        self.result = randint(1, self.size)
