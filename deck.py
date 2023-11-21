import random
from card import Card

class Deck:
    def __init__(self, num_players=int(2)):
        self.num_players = num_players
        self.cards = Card.all_cards()
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal_cards(self, num_players):
        hands = []
        cards_per_player = 2  # Количество карт для каждого игрока
        for i in range(num_players):
            hand = []
            for j in range(cards_per_player):
                if self.cards:
                    hand.append(self.cards.pop())
            hands.append(hand)
        return hands

    def draw_card(self):
        return self.cards.pop() if self.cards else None

