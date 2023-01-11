from deck import Deck
from hand import Hand


class Game:
    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        self.playerCards = []
        self.dealerCards = []

    def start_game(self):
        playGame = input("You are starting with $500. Would you like to play a hand? ")
        self.playerCards = []
        self.dealerCards = []
        if playGame.lower() == "yes":
            while self.player.balance > 0:
                self.bet = int(input("Place your bet: "))
                while self.bet < 1 or self.bet > self.player.balance:
                    if self.bet < 1:
                        print("The minimum bet is $1.")
                        break
                    print("You do not have sufficient funds.")
                    break
                self.deck.create_deck()
                self.deck.shuffle()
                self.playerCards = self.deck.deal(2)
                newPlayerCards = ", ".join(self.playerCards)
                self.dealerCards = self.deck.deal(2)
                newDealerCards = ", ".join(self.dealerCards)
                print(f"You are dealt: {newPlayerCards}")
                print(f"The dealer is dealt: {newDealerCards[:2]}, Unknown")
                action = None
                while True:
                    action = input("Would you like to hit or stay? ")
                    if action.lower() == "hit":
                        self.playerCards += Hand.add_to_hand()

                    elif action.lower() == "stand":
                        break
                    else:
                        print("That is not a valid option.")
                    newPlayerCards = ", ".join(self.playerCards)
                    print(f"You now have: {newPlayerCards}")

            print(
                "You've ran out of money. Please restart this program to try again. Goodbye."
            )
        elif playGame.lower() == "no":
            print(f"You have ${self.player.balance} left. Goodbye.")
        else:
            print("Invalid option. Please restart this program to try again. Goodbye.")
