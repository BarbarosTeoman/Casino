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
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
        return values.index(card)

    def start_game(self):
        while self.player.balance > 0:
            playGame = input(
                f"You are starting with ${int(self.player.balance)}. Would you like to play a hand? "
            )
            end = False
            if playGame.lower() == "yes" and end == False:
                lobby = False
                print(
                    "You can bet on either dragon or tiger and tie. Minimum bet is $1 for all. Place your bets in the following form."
                )
                print("dragon/tiger _ tie _")
                bet = input("Place your bets: ")
                Bet = False
                while not Bet:
                    Bet = True
                    splittedBet = bet.split(" ")
                    if "dragon" in splittedBet and "tiger" in splittedBet:
                        print("You can bet on either dragon or tiger!")
                        bet = input("Place your bets: ")
                        Bet = False
                    elif len(splittedBet) > 6 or len(splittedBet) < 2:
                        print("There is something wrong with your bet.")
                        bet = input("Place your bets: ")
                        Bet = False
                    else:
                        for i, k in enumerate(bet.split(" ")):
                            if i % 2 == 1:
                                if int(k) < 1:
                                    print("Minimum bet is $1")
                                    bet = input("Place your bets: ")
                                    Bet = False

                for i, k in enumerate(bet.split(" ")):
                    if i % 2 == 1:
                        self.player.balance -= int(k)

                self.deck.create_deck()
                self.deck.shuffle()
                dragon = self.deck.deal(1)
                tiger = self.deck.deal(1)
                print("   DRAGON         TIGER")
                print("  --------       -------")
                print(f"     {dragon[0]}              {tiger[0]}")

                def winner():
                    if dragontigerGame.value(dragon[0][0]) > dragontigerGame.value(
                        tiger[0][0]
                    ):
                        return "dragon"

                    if dragontigerGame.value(dragon[0][0]) < dragontigerGame.value(
                        tiger[0][0]
                    ):
                        return "tiger"

                    if dragontigerGame.value(dragon[0][0]) == dragontigerGame.value(
                        tiger[0][0]
                    ):
                        return "tie"

                try:
                    dragonBet = int(splittedBet[splittedBet.index("dragon") + 1])
                except:
                    dragonBet = 0
                try:
                    tigerBet = int(splittedBet[splittedBet.index("tiger") + 1])
                except:
                    tigerBet = 0
                try:
                    tieBet = int(splittedBet[splittedBet.index("tie") + 1])
                except:
                    tieBet = 0

                if winner() == "dragon":
                    if "dragon" in splittedBet:
                        self.player.balance += 2 * dragonBet
                        if dragonBet > tieBet:
                            print(
                                f"Congrats dragon won, you won {2*dragonBet - tieBet}$"
                            )
                        else:
                            print(
                                f"Sorry, eventough dragon won, you lost {tieBet - dragonBet}$, better luck next time!"
                            )
                    else:
                        print(
                            f"Sorry, dragon won, you lose {tigerBet + tieBet}$, better luck next time!"
                        )
                elif winner() == "tiger":
                    if "tiger" in splittedBet:
                        self.player.balance += 2 * tigerBet
                        if tigerBet > tieBet:
                            print(
                                f"Congrats dragon won, you won {2*tigerBet - tieBet}$"
                            )
                        else:
                            print(
                                f"Sorry, eventough dragon won, you lost {tieBet - tigerBet}$, better luck next time!"
                            )
                    else:
                        print(
                            f"Sorry, tiger won, you lose {dragonBet + tieBet}$, better luck next time!"
                        )
                elif winner() == "tie":
                    if "tie" in splittedBet:
                        self.player.balance += 10 * tieBet
                        print(
                            f"Congrats tie, you won {10*tieBet - dragonBet - tigerBet}$"
                        )
                    else:
                        print(
                            f"Sorry,it was a tie, you lose {dragonBet + tigerBet}$, better luck next time!"
                        )

            elif playGame.lower() == "no":
                lobby = True
                return lobby
            else:
                print("Invalid option.")
        print("You've ran out of money.")
        return None
