import time
from player import Player
from blackjackgame import blackjackGame
from dragontigergame import dragontigerGame

STARTING_BALANCE = 500
player = Player(STARTING_BALANCE)
blackjackgame = blackjackGame(player)
dragontigergame = dragontigerGame(player)

print("Welcome to the Casino!")
lobby = True
while lobby == True:
    time.sleep(1)
    print(
        f"You have ${player.balance}. What do you want to play? You can also just leave by typing leave."
    )
    gameChoice = input("Dragon Tiger or blackjack: ")
    print()
    if gameChoice.lower() == "leave":
        break
    elif gameChoice.lower() == "blackjack":
        lobby = blackjackgame.start_game()
time.sleep(1)
if player.balance > STARTING_BALANCE:
    print(
        f"Lucky day huh! You made ${player.balance - STARTING_BALANCE} profit today. Good bye!"
    )
elif player.balance == STARTING_BALANCE:
    print("You have the same amount as you have started with, what a waste of time.")
else:
    print(
        f"You lost ${-player.balance + STARTING_BALANCE} today. That happens, better luck on the next time!"
    )
