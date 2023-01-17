from deck import Deck
from hand import Hand
import time


class dragontigerGame:
    def __init__(self, player):
        self.player = player
        self.bet = None
        self.deck = Deck()
