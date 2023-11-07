import random
from card import Card


class Deck:
    def __init__(self, cards: list[Card] | None = None):
        if cards is None:
            self.cards = Card.all_cards()
            random.shuffle(self.cards)
        else:
            self.cards = cards

    def __repr__(self):
        return ' '.join([str(c) for c in self.cards])

    @staticmethod
    def create(text: str):
        return Deck(Card.card_list(text))
