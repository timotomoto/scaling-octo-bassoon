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

    def winner(self):
        if self.XO in board[0][0] and self.XO in board[0][1] and self.XO in board[0][2]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()
        elif self.XO in board[1][0] and self.XO in board[1][1] and self.XO in board[1][2]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()
        elif self.XO in board[2][0] and self.XO in board[2][1] and self.XO in board[2][2]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()
        elif self.XO in board[0][0] and self.XO in board[1][0] and self.XO in board[2][0]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()
        elif self.XO in board[0][1] and self.XO in board[1][1] and self.XO in board[2][1]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()
        elif self.XO in board[0][2] and self.XO in board[1][2] and self.XO in board[2][2]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()
        elif self.XO in board[0][0] and self.XO in board[1][1] and self.XO in board[2][2]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()
        elif self.XO in board[0][2] and self.XO in board[1][1] and self.XO in board[2][0]:
            print("{} wins!!".format(self.name))
            self.win = True
            quit()   
def tie():
    if " " not in board[0] and " " not in board[1] and " " not in board[2] and player1.win == False and player2.win == False:
        print("Tie")

def boardd():
    for places in board:
        print(places)
    player1.winner()
    player2.winner()
    tie()

def coin_flip(): 
    coin = random.randint(0,1)
    if coin == 0:
        return "Heads"
    return "Tails"

player1_name = input("Let's play a game of tic-tac-toe! What is your name? ")
player2_name = input("Hello " + player1_name + ", What is your opponent's name? ")