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
        """ Все карты для создания колоды. """
        return [Card(typec, value) for value in Card.VALUES for typec in Card.TYPES]


x = Card('sleep', 0)
print(x)
