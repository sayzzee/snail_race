import random


class Card:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    @staticmethod
    def create_deck():
        deck = []
        veggies = ['pepper', 'onion', 'peas', 'tomato', 'carrot', 'cucumber']
        for veggie in veggies:
            for _ in range(5):
                deck.append(VegetableCard(veggie))
        for _ in range(8):
            deck.append(NumberCard(0, False))  # спящая улитка
        for _ in range(3):
            deck.append(NumberCard(1, False))  # номер без стрелки
            deck.append(NumberCard(2, False))
            deck.append(NumberCard(3, False))
            deck.append(NumberCard(1, True))  # номер со стрелкой
            deck.append(NumberCard(2, True))
            deck.append(NumberCard(3, True))
        random.shuffle(deck)
        return deck

    @staticmethod
    def distribute_cards(players, deck):
        for player in players:
            player_cards = [deck.pop(), deck.pop()]
            player.hand = player_cards

    @staticmethod
    def draw_card(player, deck):
        if len(deck) > 0:
            player.hand.append(deck.pop())
        else:
            print("Колода пуста, больше карт нет")

class VegetableCard(Card):
    def __init__(self, veggie):
        self.veggie = veggie

    def __repr__(self):
        return f'{self.veggie}'


class NumberCard(Card):
    def __init__(self, number, arrow):
        self.number = number
        self.arrow = arrow

    def __repr__(self):
        return f'{self.number} + {self.arrow}'


