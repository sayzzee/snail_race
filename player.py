from card import Card
from ground import Field


class Player:
    HAND_SIZE = 2

    def __init__(self, name: str, field):
        self.name = name
        self.hand = None
        self.active = True  # стоит на поле
        self.position = 0   # номер ячейки от начала дистанции
        self.field = field

    def add_cards(self, cards: list[Card]):
        self.hand += cards
        if len(self.hand) > self.HAND_SIZE:
            raise ValueError(f"{self.name} Too many cards in hand :" + repr(cards))

    def move_snail(self, steps):
        self.position = min(self.position + steps, len(self.field.field) - 1)

    def move_opponent_snail(self, opponent, steps):
        opponent.position = min(opponent.position + steps, len(self.field.field) - 1)

    def exit_game(self):
        self.active = False
        self.position = -1  # Позиция -1 обозначает, что игрок выбыл из игры