import random
import pytest
from card import Card

class Deck:
    def __init__(self, num_players=2):
        self.num_players = num_players
        self.cards = Card.all_cards()
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_cards(self):
        hands = []
        for i in range(self.num_players):
            hand = []
            for j in range(2):
                if self.cards:
                    hand.append(self.cards.pop())
            hands.append(hand)
        return hands

    def draw_card(self):
        return self.cards.pop() if self.cards else None

