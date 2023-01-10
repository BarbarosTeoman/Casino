import random
from card import Card


class Deck:
    def __init__(self):
        pass

    @staticmethod
    def create_deck():
        global allCards
        allCards = []
        for value1 in Card.SUIT_SYMBOLS.values():
            for value2 in Card.VALUE_NAMES.values():
                allCards.append(f"{value2} {value1}")
        return allCards

    @staticmethod
    def shuffle():
        Deck.create_deck()
        random.shuffle(allCards)
        return allCards

    def deal(self, num_cards):
        pass


deck = Deck()
print(deck.shuffle())
