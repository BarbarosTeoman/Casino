from player import Player
from game import Game

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE)
game = Game(player)

print("Welcome to Blackjack!")
print()
game.start_game()