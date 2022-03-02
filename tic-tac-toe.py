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
coin_f = input("Ok, to see who gets to play first we will flip a coin. " + player2_name + ", Heads or Tails? ")
coin_flip_pick = coin_f.title()
while coin_flip_pick != "Heads" and coin_flip_pick != "Tails":
    coin_f = input("That wasn't one of the two options, try again. ")
    coin_flip_pick = coin_f.title()
coin_flip_result = coin_flip()
print("The coin landed on " + coin_flip_result + ".")
if coin_flip_pick == coin_flip_result:
    print("Congrats " + player2_name + ", you get to play first!")
    player1 = Player(player1_name, "O")
    player2 = Player(player2_name, "X")
    coin_flip_winner = player2
    coin_flip_loser = player1
else:
    print("Looks like " + player1_name + " gets to play first!")
    player1 = Player(player1_name, "X")
    player2 = Player(player2_name, "O")
    coin_flip_winner = player1
    coin_flip_loser = player2
print(player1)
print(player2)
print("To play you will type which location you want to play at.")
coard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
print("e.g;")
for num in coard:
    print(num)
choice = input("Ok, {} where will you play? ".format(coin_flip_winner.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
    choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
    choice = input("That was already played, try something else. ")
coin_flip_winner.play(int(choice)-1)
boardd()
choice = input("OK {}, it's your turn. ".format(coin_flip_loser.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_loser.play(int(choice)-1)
boardd()
choice = input("{} turn! ".format(coin_flip_winner.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_winner.play(int(choice)-1)
boardd()
choice = input("{} turn! ".format(coin_flip_loser.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_loser.play(int(choice)-1)
boardd()
choice = input("{} turn! ".format(coin_flip_winner.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_winner.play(int(choice)-1)
boardd()
choice = input("{} turn! ".format(coin_flip_loser.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_loser.play(int(choice)-1)
boardd()
choice = input("{} turn! ".format(coin_flip_winner.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_winner.play(int(choice)-1)
boardd()
choice = input("{} turn! ".format(coin_flip_loser.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_loser.play(int(choice)-1)
boardd()
choice = input("{} turn! ".format(coin_flip_winner.name))
while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9":
  choice = input("whoops, something went wrong try again. ")
while int(choice)-1 not in numbers:
  choice = input("That was already played, try something else. ")
coin_flip_winner.play(int(choice)-1)
boardd()
