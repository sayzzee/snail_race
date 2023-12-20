from card_newV import VegetableCard, NumberCard

class Snail:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.sleeping = False
        self.hand = []

    def __repr__(self):
        return f'{self.name}'

    def move(self, steps):
        self.position += steps

    def push(self, steps):
        self.position += steps

    def sleep(self):
        self.sleeping = True

    def wakeup(self):
        self.sleeping = False

    def show_hand(self):
        print(f"Карты в руке улитки {self.name}:")
        for i, card in enumerate(self.hand):
            if isinstance(card, VegetableCard):
                target_veggie = card.veggie
                print(f"{i}: Карта овоща ({target_veggie})")
            elif isinstance(card, NumberCard):
                card_type = "со стрелкой" if card.arrow else "без стрелки"
                print(f"{i}: Карта с номером ({card.number}) - Тип: {card_type}")

    def next_player(self, players, current_player_index):
        current_player_index = (current_player_index + 1) % len(players)
        return current_player_index
