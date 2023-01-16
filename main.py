from player import Player
from blackjack.game import Game

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE)
game = Game(player)

print("Welcome to the Casino!")
print("What do you want to play? Dragon Tiger or blackjack: ")
print()
game.start_game()
