from deck import Deck
from hand import Hand
import time


class blackjackGame:
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
        value = 0
        if any("A" in sub for sub in card):
            listOfA = []
            for i in card:
                if i[0] == "A":
                    listOfA.append(i[0])
            for i in card:
                if i[0] in ["T", "K", "Q", "J"]:
                    value += 10
                elif i[0] != "A":
                    value += int(i[0])
            if value + (len(listOfA) * 11) <= 21:
                return value + (len(listOfA) * 11)
            elif value + 11 + (len(listOfA) - 1) * 1 <= 21:
                return value + 11 + (len(listOfA) - 1) * 1
            else:
                return value + (len(listOfA))
        else:
            for i in card:
                if i[0] in ["T", "K", "Q", "J"]:
                    value += 10
                else:
                    value += int(i[0])
            return value

    def start_game(self):
        while self.player.balance > 0:
            playGame = input(
                f"You are starting with ${int(self.player.balance)}. Would you like to play a hand? "
            )
            self.playerCards = []
            self.dealerCards = []
            self.playerCardValue = []
            self.dealerCardValue = []

            end = False

            if playGame.lower() == "yes" and end == False:
                lobby = False
                self.bet = input("Place your bet: ")
                if self.bet == "all in":
                    self.bet = self.player.balance
                self.bet = int(self.bet)
                while self.bet < 1 or self.bet > self.player.balance:
                    if self.bet < 1:
                        print("The minimum bet is $1.")
                        self.bet = int(input("Place your bet: "))
                    else:
                        print("You do not have sufficient funds.")
                        self.bet = int(input("Place your bet: "))

                self.deck.create_deck()
                self.deck.shuffle()
                self.playerCards = self.deck.deal(2)
                self.playerCardValue.append(blackjackGame.value(self.playerCards))
                newPlayerCards = ", ".join(self.playerCards)
                self.dealerCards = self.deck.deal(2)
                self.dealerCardValue.append(blackjackGame.value(self.dealerCards))
                newDealerCards = ", ".join(self.dealerCards)
                print(f"You are dealt: {newPlayerCards}")
                print(f"The dealer is dealt: {newDealerCards[:2]}, Unknown")
                action = None

                if sum(self.playerCardValue) == 21 and end == False:
                    print(f"The dealer has: {newDealerCards}")
                    if sum(self.dealerCardValue) == 21:
                        print(
                            f"You both have blackjacks, it is a push. You got your money back."
                        )
                        end = True
                    else:
                        print(f"You won ${1.5*self.bet} :)")
                        end = True
                        self.player.balance += 1.5 * self.bet

                if self.dealerCards[0][0] == "A" and end == False:
                    if self.player.balance > 1.5 * self.bet:
                        insurance = input(
                            "The insurance bet is now open, do you want to insure? "
                        )
                        if insurance.lower() == "yes":
                            if sum(self.dealerCardValue) == 21:
                                print("The dealer has blackjack.")
                                print("You got your money back.")
                                end = True
                            print("There is no blackjack, the game keeps going.")
                            self.bet *= 1.5
                        else:
                            if sum(self.dealerCardValue) == 21:
                                print("The dealer has blackjack.")
                                print(f"You lost ${self.bet} :(")
                                end = True
                                self.player.balance -= self.bet
                    else:
                        print("You don't have enough money to insure.")
                        if sum(self.dealerCardValue) == 21:
                            print("The dealer has blackjack.")
                            print(f"You lost ${self.bet} :(")
                            end = True
                            self.player.balance -= self.bet
                        else:
                            print("There is no blackjack, the game keeps going.")

                doubling = True

                while end == False:
                    if doubling:
                        action = input("Would you like to hit, stand or double? ")
                    else:
                        action = input("Would you like to hit or stand? ")
                    if action.lower() == "hit":
                        doubling = False
                        newCard = Hand.add_to_hand()
                        self.playerCards += newCard
                        self.playerCardValue.pop()
                        self.playerCardValue.append(
                            blackjackGame.value(self.playerCards)
                        )
                        newPlayerCards = ", ".join(self.playerCards)
                        print(f"You now have: {newPlayerCards}")
                        if sum(self.playerCardValue) > 21:
                            print(f"It is too many, you busted. You lose ${self.bet}.")
                            self.player.balance -= self.bet
                            end = True
                            break
                        if sum(self.playerCardValue) == 21:
                            newDealerCards = ", ".join(self.dealerCards)
                            print(f"The dealer has: {newDealerCards}")
                            while sum(self.dealerCardValue) < 17:
                                newCard = Hand.deck.deal(1)[:2]
                                time.sleep(1)
                                print(f"Dealer hits and is dealt: {newCard[0]}")
                                self.dealerCards += newCard
                                self.dealerCardValue.pop()
                                self.dealerCardValue.append(
                                    blackjackGame.value(self.dealerCards)
                                )
                                newDealerCards = ", ".join(self.dealerCards)
                                time.sleep(1)
                                print(f"The dealer has: {newDealerCards}")
                                if sum(self.dealerCardValue) > 21:
                                    time.sleep(1)
                                    print(
                                        f"It is a {len(self.dealerCards)} card bust for the dealer, you win ${self.bet} :)"
                                    )
                                    self.player.balance += self.bet
                                    end = True
                                    break
                            if end == False:
                                time.sleep(1)
                                print("Dealer stands.")
                                if sum(self.dealerCardValue) > sum(
                                    self.playerCardValue
                                ):
                                    time.sleep(1)
                                    print(f"The dealer wins, you lose ${self.bet} :(")
                                    self.player.balance -= self.bet
                                    end = True
                                    break
                                elif sum(self.dealerCardValue) == sum(
                                    self.playerCardValue
                                ):
                                    time.sleep(1)
                                    print("It is a push. Your bet has been returned.")
                                    end = True
                                    break
                                else:
                                    time.sleep(1)
                                    print(f"You win ${self.bet}!")
                                    self.player.balance += self.bet
                                    end = True
                                    break
                    elif action.lower() == "stand" and end == False:
                        newDealerCards = ", ".join(self.dealerCards)
                        time.sleep(1)
                        print(f"The dealer has: {newDealerCards}")
                        while sum(self.dealerCardValue) < 17:
                            newCard = Hand.deck.deal(1)[:2]
                            time.sleep(1)
                            print(f"Dealer hits and is dealt: {newCard[0]}")
                            self.dealerCards += newCard
                            self.dealerCardValue.pop()
                            self.dealerCardValue.append(
                                blackjackGame.value(self.dealerCards)
                            )
                            newDealerCards = ", ".join(self.dealerCards)
                            time.sleep(1)
                            print(f"The dealer has: {newDealerCards}")
                            if sum(self.dealerCardValue) > 21:
                                time.sleep(1)
                                print(
                                    f"It is a {len(self.dealerCards)} card bust for the dealer, you win ${self.bet} :)"
                                )
                                self.player.balance += self.bet
                                end = True
                                break
                        if end == False:
                            time.sleep(1)
                            print("Dealer stands.")
                            if sum(self.dealerCardValue) > sum(self.playerCardValue):
                                time.sleep(1)
                                print(f"The dealer wins, you lose ${self.bet} :(")
                                self.player.balance -= self.bet
                                end = True
                                break
                            elif sum(self.dealerCardValue) == sum(self.playerCardValue):
                                time.sleep(1)
                                print("It is a push. Your bet has been returned.")
                                end = True
                                break
                            else:
                                time.sleep(1)
                                print(f"You win ${self.bet}!")
                                self.player.balance += self.bet
                                end = True
                                break
                    elif action.lower() == "double" and end == False and doubling:
                        if self.player.balance < 2 * self.bet:
                            print("You don't have enough money to double down.")
                            continue
                        else:
                            newCard = Hand.add_to_hand()
                            self.playerCards += newCard
                            self.playerCardValue.pop()
                            self.playerCardValue.append(
                                blackjackGame.value(self.playerCards)
                            )
                            newPlayerCards = ", ".join(self.playerCards)
                            print(f"You now have: {newPlayerCards}")
                            if sum(self.playerCardValue) > 21:
                                print(
                                    f"It is too many, you busted. You lose ${2*self.bet}."
                                )
                                self.player.balance -= 2 * self.bet
                                end = True
                                break
                            newDealerCards = ", ".join(self.dealerCards)
                            time.sleep(1)
                            print(f"The dealer has: {newDealerCards}")
                            while sum(self.dealerCardValue) < 17:
                                newCard = Hand.deck.deal(1)[:2]
                                time.sleep(1)
                                print(f"Dealer hits and is dealt: {newCard[0]}")
                                self.dealerCards += newCard
                                self.dealerCardValue.pop()
                                self.dealerCardValue.append(
                                    blackjackGame.value(self.dealerCards)
                                )
                                newDealerCards = ", ".join(self.dealerCards)
                                time.sleep(1)
                                print(f"The dealer has: {newDealerCards}")
                                if sum(self.dealerCardValue) > 21:
                                    time.sleep(1)
                                    print(
                                        f"It is a {len(self.dealerCards)} card bust for the dealer, you win ${2*self.bet} :)"
                                    )
                                    self.player.balance += 2 * self.bet
                                    end = True
                                    break
                            if end == False:
                                time.sleep(1)
                                print("Dealer stands.")
                                if sum(self.dealerCardValue) > sum(
                                    self.playerCardValue
                                ):
                                    print(f"The dealer wins, you lose ${2*self.bet} :(")
                                    self.player.balance -= 2 * self.bet
                                    end = True
                                    break
                                elif sum(self.dealerCardValue) == sum(
                                    self.playerCardValue
                                ):
                                    print("It is a push. Your bet has been returned.")
                                    end = True
                                    break
                                else:
                                    print(f"You win ${2*self.bet}!")
                                    self.player.balance += 2 * self.bet
                                    end = True
                                    break
                    else:
                        print("That is not a valid option.")
            elif playGame.lower() == "no":
                lobby = True
                return lobby
            else:
                print("Invalid option.")
        print("You've ran out of money.")
        return None
