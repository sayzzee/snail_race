import pytest
import random


class Card:
    TYPES = ['sleep', 'vegetable', 'go', 'go_last']
    VALUES = [1, 2, 3]
    GAME_RULES = {
        'sleep': 'not move',
        'vegetable': 'move to nearest vegetable',
        'go': 'go n steps',
        'go_last': 'go n steps (last)'
    }

    VEGETABLES = ['pepper', 'onion', 'peas', 'tomato', 'carrot', 'cucumber']

    COUNT_CARDS = {
        'vegetables': 30,
        'sleep': 8,
        'go': 6,
        'go_last': 6
    }

    def __init__(self, typec, value, game_rule=""):
        if typec in self.TYPES:
            self.typec = typec
        else:
            raise ValueError(f'Неверный тип карты {typec}')

        if typec == 'go' or typec == 'go_last':
            if value in self.VALUES:
                self.value = value
            else:
                raise ValueError(f'Неверное значение карты {value}')
        else:
            self.value = 0
        if typec in self.GAME_RULES:
            self.game_rule = game_rule

    def __repr__(self):
        if self.game_rule != "":
            if self.typec == "sleep" or self.typec == "vegetable":
                return f'{self.typec}'
            else:
                return f'{self.typec}:{self.value} - {self.game_rule}'
        return f'{self.typec}:{self.value}'

    @staticmethod
    def create():
        type_card = random.choice(Card.TYPES)
        value_card = random.choice(Card.VALUES)
        card = Card(type_card, value_card)
        return card

    @staticmethod
    def all_cards():
        all_cards = []
        for i in range(5):
            for j in range(len(Card.VEGETABLES)):
                all_cards.append(Card.VEGETABLES[j] + ': 0')
        for i in range(8):
            all_cards.append(Card.TYPES[0] + ': 0')
        for i in range(3):
            all_cards.append(Card.TYPES[2] + ': ' + str(i + 1))
            all_cards.append(Card.TYPES[3] + ': ' + str(i + 1))
            all_cards.append(Card.TYPES[2] + ': ' + str(i + 1))
            all_cards.append(Card.TYPES[3] + ': ' + str(i + 1))

        if len(all_cards) != 50:
            raise ValueError(f'Колода не может существовать')
        return print(all_cards)

x = Card('go', 1)
y = Card.all_cards()