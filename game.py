from deck import Deck
from hand import Hand


class Game:
    def __init__(self, player):
        self.player = player
        self.bet = None
        self.deck = Deck()
        self.playerCards = []
        self.dealerCards = []
        self.playerCardValue = []
        self.dealerCardValue = []

    @staticmethod
    def value(card):
        if card[0] in ["T", "K", "Q", "J"]:
            return 10
        elif card[0] == "A":
            return 11
        else:
            return int(card[0])

    def start_game(self):
        while self.player.balance > 0:
            playGame = input(
                f"You are starting with ${self.player.balance}. Would you like to play a hand? "
            )
            self.playerCards = []
            self.dealerCards = []
            self.playerCardValue = []
            self.dealerCardValue = []

            end = False

            if playGame.lower() == "yes" and end == False:
                self.bet = int(input("Place your bet: "))
                while self.bet < 1 or self.bet > self.player.balance:
                    if self.bet < 1:
                        print("The minimum bet is $1.")
                        self.bet = int(input("Place your bet: "))
                        break
                    print("You do not have sufficient funds.")
                    self.bet = int(input("Place your bet: "))
                    break
                self.deck.create_deck()
                self.deck.shuffle()
                self.playerCards = self.deck.deal(2)
                for i in self.playerCards:
                    self.playerCardValue.append(Game.value(i))
                newPlayerCards = ", ".join(self.playerCards)
                self.dealerCards = self.deck.deal(2)
                for i in self.dealerCards:
                    self.dealerCardValue.append(Game.value(i))
                newDealerCards = ", ".join(self.dealerCards)
                print(f"You are dealt: {newPlayerCards}")
                print(f"The dealer is dealt: {newDealerCards[:2]}, Unknown")
                action = None
                while end == False:
                    action = input("Would you like to hit or stand? ")
                    if action.lower() == "hit":
                        newCard = Hand.add_to_hand()
                        self.playerCards += newCard
                        self.playerCardValue.append(Game.value(newCard[0]))
                        if sum(self.playerCardValue) > 21:
                            print(f"It is too many, you busted. You lose ${self.bet}.")
                            self.player.balance -= self.bet
                            end = True
                            break
                    elif action.lower() == "stand" and end == False:
                        newDealerCards = ", ".join(self.dealerCards)
                        print(f"The dealer has: {newDealerCards}")
                        while sum(self.dealerCardValue) < 17:
                            newCard = Hand.deck.deal(1)[:2]
                            print(f"Dealer hits and is dealt: {newCard[0]}")
                            self.dealerCards += newCard
                            self.dealerCardValue.append(Game.value(newCard[0]))
                            newDealerCards = ", ".join(self.dealerCards)
                            print(f"The dealer has: {newDealerCards}")
                            if sum(self.dealerCardValue) > 21:
                                print(f"The dealer busts, you win ${self.bet} :)")
                                self.player.balance += self.bet
                                end = True
                                break
                        if end == False:
                            print("Dealer stands.")
                            if sum(self.dealerCardValue) > sum(self.playerCardValue):
                                print(f"The dealer wins, you lose ${self.bet} :(")
                                self.player.balance -= self.bet
                                end = True
                                break
                            elif sum(self.dealerCardValue) == sum(self.playerCardValue):
                                print("You tie. Your bet has been returned.")
                                end = True
                                break
                            else:
                                print(f"You win ${self.bet}!")
                                self.player.balance += self.bet
                                end = True
                                break
                    else:
                        print("That is not a valid option.")
                    newPlayerCards = ", ".join(self.playerCards)
                    print(f"You now have: {newPlayerCards}")
            elif playGame.lower() == "no":
                print(f"You have ${self.player.balance} left. Goodbye.")
                return None
            else:
                print("Invalid option.")
        print(
            "You've ran out of money. Please restart this program to try again. Goodbye."
        )
        return None
