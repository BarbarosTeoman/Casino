import random
from card import Card


class Deck:

    allCards = []

    def __init__(self):
        pass

    @staticmethod
    def create_deck():
        for value1 in Card.SUIT_SYMBOLS.values():
            for value2 in Card.VALUE_NAMES.values():
                Deck.allCards.append(f"{value2}{value1}")
        return Deck.allCards

    @staticmethod
    def shuffle():
        random.shuffle(Deck.allCards)
        return Deck.allCards

    def deal(self, num_cards):
        dealtCards = Deck.allCards[:num_cards]
        for Cards in dealtCards:
            Deck.allCards.remove(Cards)
        return dealtCards

