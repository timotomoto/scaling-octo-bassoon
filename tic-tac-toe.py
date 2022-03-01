import random
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Player:
  def __init__(self, name, XO):
    self.name = name
    self.XO = XO
    self.win = False