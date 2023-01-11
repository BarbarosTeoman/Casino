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
        self.playerCardValue = []
        self.dealerCardValue = []

    def start_game(self):
        while self.player.balance > 0:
            playGame = input(
                f"You are starting with ${self.player.balance}. Would you like to play a hand? "
            )
            self.playerCards = []
            self.dealerCards = []
            self.playerCardValue = []
            self.dealerCardValue = []

            def value(card):
                if card[0] in ["T", "K", "Q", "J"]:
                    return 10
                elif card[0] == "A":
                    return 11
                else:
                    return card[0]

            if playGame.lower() == "yes":
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
                for i in self.playerCards:
                    self.playerCardValue.append(value(i))
                newPlayerCards = ", ".join(self.playerCards)
                self.dealerCards = self.deck.deal(2)
                for i in self.dealerCards:
                    self.dealerCardValue.append(value(i))
                newDealerCards = ", ".join(self.dealerCards)
                print(f"You are dealt: {newPlayerCards}")
                print(f"The dealer is dealt: {newDealerCards[:2]}, Unknown")
                action = None
                while True:
                    action = input("Would you like to hit or stay? ")
                    if action.lower() == "hit":
                        self.playerCards += Hand.add_to_hand()
                        self.playerCardValue.append(value(i))
                    elif action.lower() == "stand":
                        break
                    else:
                        print("That is not a valid option.")
                    newPlayerCards = ", ".join(self.playerCards)
                    print(
                        f"You now have: {newPlayerCards} your new card value is {sum(self.playerCardValue)}"
                    )
            elif playGame.lower() == "no":
                print(f"You have ${self.player.balance} left. Goodbye.")
                return None
            else:
                print(
                    "Invalid option. Please restart this program to try again. Goodbye."
                )
        print(
            "You've ran out of money. Please restart this program to try again. Goodbye."
        )
        return None
