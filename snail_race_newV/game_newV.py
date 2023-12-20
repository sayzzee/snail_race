import random
import json
from card_newV import VegetableCard, NumberCard
from snail_newV import Snail

class SnailRaceGame:
    def __init__(self, players):
        self.players = players
        empty_cell = '________'
        FIELD = [
            ['cucumber', 'peas', 'carrot', 'pepper', 'onion', 'tomato'],
            ['pepper', 'onion', 'cucumber', 'peas', 'tomato', 'carrot'],
            ['peas', 'tomato', 'pepper', 'carrot', 'cucumber', 'onion'],
            ['cucumber', 'pepper', 'onion', 'carrot', 'peas', 'tomato']
        ]
        for i in range(4):
            side = random.randrange(-1, 2, 2)
            FIELD[i] = FIELD[i][::side]
            random.shuffle(FIELD)

        field = [veggie for sublist in FIELD for veggie in sublist]
        field.insert(0, empty_cell)
        self.field = field
        self.active_snails = players.copy()
        self.current_player_index = 0
        self.deck = self.create_deck()
        self.distribute_cards()

    def __repr__(self):
        return (f'{self.players}\n{self.field}\n{self.deck}')

    def create_deck(self):
        deck = []
        veggies = ['перец', 'лук', 'горох', 'помидор', 'морковь', 'огурец']
        for veggie in veggies:
            for _ in range(5):
                deck.append(VegetableCard(veggie))
        for _ in range(8):
            deck.append(NumberCard(0, False))  # спящая улитка
        for _ in range(3):
            deck.append(NumberCard(1, False))  # номер без стрелки
            deck.append(NumberCard(2, False))
            deck.append(NumberCard(3, False))
            deck.append(NumberCard(1, True))   # номер со стрелкой
            deck.append(NumberCard(2, True))
            deck.append(NumberCard(3, True))
        random.shuffle(deck)
        return deck

    def distribute_cards(self):
        for player in self.players:
            player_cards = [self.deck.pop(), self.deck.pop()]
            player.hand = player_cards

    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def draw_card(self, player):
        if len(self.deck) > 0:
            player.hand.append(self.deck.pop())
        else:
            print("Колода пуста, больше карт нет")

    def display_field_with_snails(self):
        field_with_snails = self.field.copy()

        # Сохранение овощей на позициях улиток
        veggie_positions = {i: self.field[i] for i, veggie in enumerate(self.field) if veggie != '________'}

        # Помещаем улитки на поле
        positions = {}
        for player in self.active_snails:
            if player.position not in positions:
                positions[player.position] = [f"{player.name[0].upper()}"]
            else:
                positions[player.position].append(f"{player.name[0].upper()}")

        for position, snails in positions.items():
            if len(snails) > 1:
                field_with_snails[position] = ''.join(snails)
            else:
                field_with_snails[position] = snails[0]

        # Выводим поле с улитками
        for i in range(5):
            row = field_with_snails[i * 5:(i + 1) * 5]
            for index, item in enumerate(row):
                if item != '________':
                    if field_with_snails[i * 5 + index] != item and index > 0:
                        row[index] = f"[{field_with_snails[i * 5 + index]}({item})]"
                    else:
                        row[index] = f"[{item}]"

            # Восстановление овощей после ухода улитки
            for j in range(i * 5, (i + 1) * 5):
                if j in veggie_positions and field_with_snails[j] == '':
                    field_with_snails[j] = veggie_positions[j]

            print('  '.join(row))

    def play_card(self, card_index):
        current_player = self.players[self.current_player_index]
        card = current_player.hand.pop(card_index)
        if isinstance(card, VegetableCard):
            current_veggie = card.veggie
            found_veggie_position = None
            for i in range(current_player.position + 1, len(self.field)):
                if self.field[i] == current_veggie:
                    found_veggie_position = i
                    break
            if found_veggie_position is not None:
                self.field[current_player.position] = ''
                current_player.position = found_veggie_position
                self.field[current_player.position] = current_veggie
        elif isinstance(card, NumberCard):
            if card.arrow:
                # двигаем улитку с самой маленькой позицией
                min_snail = min(self.active_snails, key=lambda x: x.position)
                min_snail.move(card.number)
            else:
                # двигаем улитку игрока, который играет карту
                current_player.move(card.number)
                for snail in self.active_snails:
                    if snail != current_player and snail.position == current_player.position:
                        snail.move(card.number)
        self.draw_card(current_player)

    def check_winner(self):
        remaining_snails = [snail for snail in self.active_snails if snail.position < len(self.field)]
        if len(remaining_snails) == 1:
            return remaining_snails[0]
        return None

    def show_hand(self):
        current_player = self.players[self.current_player_index]
        print(f"Карты в руке игрока {current_player.name}:")
        for i, card in enumerate(current_player.hand):
            if isinstance(card, VegetableCard):
                target_veggie = card.veggie
                print(f"{i}: Карта овоща ({target_veggie})")
            elif isinstance(card, NumberCard):
                card_type = "со стрелкой" if card.arrow else "без стрелки"
                print(f"{i}: Карта с номером ({card.number}) - Тип: {card_type}")

    def find_nearest_veggie_position(self, target_veggie, current_position):
        veggie_positions = [i for i, veggie in enumerate(self.field) if veggie == target_veggie]
        if not veggie_positions:
            return "нет такого овоща на поле"

        distances = [abs(pos - current_position) for pos in veggie_positions]
        nearest_position = veggie_positions[distances.index(min(distances))]
        return nearest_position

    def save_game_to_json(self, filename):
        game_state = {
            "players": [
                {"name": player.name, "position": player.position, "sleeping": player.sleeping,
                 "hand": [card.__dict__ for card in player.hand]}
                for player in self.players
            ],
            "field": self.field,
            "active_snails": [snail.name for snail in self.active_snails],
            "current_player_index": self.current_player_index,
            "deck": [card.__dict__ for card in self.deck]
        }

        with open(filename, 'w') as file:
            json.dump(game_state, file)

    def load_game_from_json(self, filename):
        with open(filename, 'r') as file:
            game_state = json.load(file)

        # Restore players
        for i, player_state in enumerate(game_state["players"]):
            self.players[i].position = player_state["position"]
            self.players[i].sleeping = player_state["sleeping"]
            self.players[i].hand = [VegetableCard(card["veggie"]) if "veggie" in card
                                    else NumberCard(card["number"], card["arrow"]) for card in player_state["hand"]]

        # Restore field, active snails, current player index, and deck
        self.field = game_state["field"]
        self.active_snails = [snail for snail in self.players if snail.name in game_state["active_snails"]]
        self.current_player_index = game_state["current_player_index"]
        self.deck = [VegetableCard(card["veggie"]) if "veggie" in card
                     else NumberCard(card["number"], card["arrow"]) for card in game_state["deck"]]