from deck import Deck


class Hand:

    deck = Deck()

    def __init__(self):
        self.deck = Deck()

    def get_value(self):
        pass

    @staticmethod
    def add_to_hand():
        newCard = Hand.deck.deal(1)[:2]
        print(f"You are dealt: {newCard[0]}")
        return newCard

    def __str__(self):
        pass
