from card import Card
from deck import Deck
from ground import Field

class Game:
    def __init__(self):
        self.deck = Deck()  # Создаем пустую колоду
        self.players = []   # Список игроков
        self.field = Field()
        self.player_positions = {}  # Словарь для отслеживания позиций игроков на поле
        self.active_players = []    # Список активных игроков

    def add_player(self, player_name):
        self.players.append(player_name)
        self.active_players.append(player_name)

    def start_game(self):
        # Проверяем наличие игроков и добавляем двух игроков по умолчанию, если их нет
        if len(self.players) == 0:
            print("Добавлено два игрока по умолчанию.")
            self.add_player("Player 1")
            self.add_player("Player 2")

        self.deck.cards = Card.all_cards()  # Заполняем колоду картами из Card.all_cards()
        self.deck.shuffle_deck()  # Перемешиваем колоду
        self.deal_initial_cards()  # Раздаем карты игрокам

    def deal_initial_cards(self):
        hands = self.deck.deal_cards(len(self.players))  # Раздаем карты игрокам
        for i, player in enumerate(self.players):
            print(f"{player} получил карты: {hands[i]}")

    def display_game_field(self):
        field_representation = Field()
        print(field_representation)

    def play_game(self):
        self.display_game_field()  # Показать начальное поле
        while len(self.active_players) > 1:
            current_player = self.players[self.player_index]
            print(f"\nХод игрока {current_player}")
            self.execute_turn(current_player)
            self.player_index = (self.player_index + 1) % len(self.players)
            self.display_game_field()  # Показать поле после хода

        print(f"Игра завершена! {self.active_players[0]} победил!")

    def execute_turn(self, current_player):
        hand = self.deck.draw_card()  # Вместо deal_cards() используем draw_card() для одной карты
        if hand:
            print(f"{current_player} получил карту: {hand}")
            self.apply_card_effect(current_player, hand)
        else:
            print("Колода пуста!")

    def apply_card_effect(self, player, card):
        card_type, value = card.split(':')
        if card_type == 'vegetable':
            self.move_to_nearest_vegetable(player, value)
        elif card_type == 'sleep':
            print(f"{player} пропускает ход.")
        elif card_type == 'go':
            self.move_forward(player, int(value))
        elif card_type == 'go_last':
            self.move_slowest_forward(player, int(value))

    def move_to_nearest_vegetable(self, player, vegetable):
        current_position = self.player_positions[player]
        current_row = self.field.field[current_position]
        next_index = (current_row.index(vegetable) + 1) % len(current_row)
        next_cell = current_row[next_index]

        if next_cell not in self.player_positions.values():
            self.player_positions[player] = next_cell
            print(f"{player} двигается к ближайшему {vegetable} на клетку {next_cell}")
        else:
            print(f"На клетке {next_cell} уже находится другая улитка!")

    def move_forward(self, player, steps):
        current_position = self.player_positions[player]
        new_position = min(current_position + steps, len(self.field.field) - 1)
        self.player_positions[player] = new_position
        print(f"{player} двигается вперед на {steps} клеток")

    def move_slowest_forward(self, player, steps):
        sorted_players = sorted(self.player_positions, key=lambda x: self.player_positions[x])
        slowest_player = sorted_players[0]
        self.move_forward(slowest_player, steps)


game = Game()
game.start_game()
