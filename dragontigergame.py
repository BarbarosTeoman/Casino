from deck import Deck
from hand import Hand
import time


class dragontigerGame:
    def __init__(self, player):
        self.player = player
        self.bets = []
        self.deck = Deck()

    @staticmethod
    def value(card):
        values = ["A","1","2","3","4","5","6","7","8","9","T","J","Q","K"]
        return values.index(card)

    def start_game(self):
        while self.player.balance > 0:
            playGame = input(
                f"You are starting with ${int(self.player.balance)}. Would you like to play a hand? "
            )
            end = False
            if playGame.lower() == "yes" and end == False:
                lobby = False
                print("You can bet on either dragon or tiger, tie and perfect tie. Minimum bet is $1 for all. Place your bets in the following form.")
                print("dragon # tie # ptie #")
                bet = input("Place your bets: ")
                Bet = False
                while not Bet:
                    Bet = True
                    splittedBet = bet.split(" ")
                    if "dragon" in splittedBet and "tiger" in splittedBet:
                        print("You can bet on either dragon or tiger!")
                        bet = input("Place your bets: ")
                        Bet = False
                    else:
                        for i,k in enumerate(bet.split(" ")):
                            if i % 2 == 1:
                                if int(k) < 1:
                                    print("Minimum bet is $1")
                                    bet = input("Place your bets: ")
                                    Bet = False

                for i,k in enumerate(bet.split(" ")):
                    if i % 2 == 1:
                        self.player.balance -= int(k)

                self.deck.create_deck()
                self.deck.shuffle()
                dragon = self.deck.deal(1)
                tiger = self.deck.deal(1)
                print("   DRAGON         TIGER")
                print("  --------       -------")
                print(f"   {dragon}      {tiger}")

                def winner():
                    if dragontigerGame.value(dragon[0]) > dragontigerGame.value(tiger[0]):
                        return "dragon"

                    if dragontigerGame.value(dragon[0]) < dragontigerGame.value(tiger[0]):
                        return "tiger"
                    
                    if dragontigerGame.value(dragon[0]) == dragontigerGame.value(tiger[0]):
                        return "tie"
                
                dragonBet = int(splittedBet[splittedBet.index("dragon")+1])
                tigerBet = int(splittedBet[splittedBet.index("tiger")+1])
                tieBet = int(splittedBet[splittedBet.index("tie")+1])
                ptieBet = int(splittedBet[splittedBet.index("ptie")+1])

                if winner() == "dragon":
                    if "dragon" in splittedBet:
                        self.player.balance += 2*dragonBet
                        print(f"Congrats dragon won, you won {2*dragonBet}")
                    else:
                        print(f"Congrats dragon won, you won {2*dragonBet}")


            elif playGame.lower() == "no":
                lobby = True
                return lobby
            else:
                print("Invalid option.")
        print("You've ran out of money.")
        return None

                
