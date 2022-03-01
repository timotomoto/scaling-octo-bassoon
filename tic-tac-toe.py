import random
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Player:
    def __init__(self, name, XO):
        self.name = name
        self.XO = XO
        self.win = False

    def __repr__(self):
        return "{name} is playing {XO}".format(name=self.name, XO=self.XO)

    def play(self, place):
        numbers.remove(place)
        if place <= 2:
            board[0].pop(place)
            board[0].insert(place, self.XO)
        elif place <= 5:
            board[1].pop(place-3)
            board[1].insert(place-3, self.XO)
        elif place <= 8:
            board[2].pop(place-6)
            board[2].insert(place-6, self.XO)
            