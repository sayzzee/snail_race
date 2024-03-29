import random

class Card:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.typec}:{self.value}'

    @staticmethod
    def all_cards():
        sleep_cards = SleepCard.create_deck()
        vegetable_cards = VegetableCard.create_deck()
        go_cards = GoCard.create_deck()
        go_last_cards = GoLastCard.create_deck()

        full_deck = sleep_cards[:8] + vegetable_cards + go_cards[:6] + go_last_cards[:6]


        return full_deck

class SleepCard(Card):
    def __init__(self):
        super().__init__(0)
        self.typec = 'sleep'
        self.game_rule = 'not move'

    @staticmethod
    def create_deck():
        deck = [SleepCard() for _ in range(8)]
        return deck

class VegetableCard(Card):
    VEGETABLES = ['pepper', 'onion', 'peas', 'tomato', 'carrot', 'cucumber']

    def __init__(self, vegetable):
        super().__init__(0)
        self.typec = 'vegetable'
        self.game_rule = f'move to nearest {vegetable}'

    @staticmethod
    def create_deck():
        deck = []
        for i in range(5):
            for j in range(len(VegetableCard.VEGETABLES)):
                veg = VegetableCard.VEGETABLES[j] + ':0'
                deck.append(str(veg))
        return deck

class GoCard(Card):
    def __init__(self, value):
        super().__init__(value)
        self.typec = 'go'
        self.game_rule = f'go {value} steps'

    @staticmethod
    def create_deck():
        deck = [GoCard(value) for value in range(1, 4) for _ in range(2)]
        return deck

class GoLastCard(Card):
    def __init__(self, value):
        super().__init__(value)
        self.typec = 'go_last'
        self.game_rule = f'go {value} steps (last)'

    @staticmethod
    def create_deck():
        deck = [GoLastCard(value) for value in range(1, 4) for _ in range(2)]
        return deck


full_deck = Card.all_cards()
print(full_deck)