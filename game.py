from card import Card
from deck import Deck
from ground import Field

class Game:
    def __init__(self):
        self.deck = Deck()  # Создаем пустую колоду
        self.players = []   # Список игроков
        self.field = Field()
        self.player_positions = {}  # Словарь для отслеживания позиций игроков на поле
        self.active_players = 0    # количество активных игроков
        self.player_index = 0       # индекс текущего игрока

    def add_player(self, player_name):
        self.players.append(player_name)
        self.active_players += 1

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
        for player in self.players:
            player.add_cards(self.deck.deal_cards())

        # hands = self.deck.deal_cards(len(self.players))  # Раздаем карты игрокам
        # for i, player in enumerate(self.players):
        #     print(f"{player} получил карты: {hands[i]}")

    def display_game_field(self):
        field_representation = Field()
        print(field_representation)

    def play_game(self):
        self.display_game_field()  # Показать начальное поле
        while self.active_players > 1:
            current_player = self.players[self.player_index]
            if not current_player.active:
                continue
            print(f"\nХод игрока {current_player}")
            self.execute_turn(current_player)
            self.player_index = (self.player_index + 1) % len(self.players)
            self.display_game_field()  # Показать поле после хода

        print(f"Игра завершена! {self.active_players[0]} победил!")

    def execute_turn(self, current_player: Player):
        card = current_player.choose_card()
        self.apply_card_effect(current_player, card)

        # TODO: берем карту, кладем в руку и все, забиваем на пустую колоду raise
        hand = self.deck.draw_card()  # Вместо deal_cards() используем draw_card() для одной карты
        if hand:
            print(f"{current_player} получил карту: {hand}")
            self.apply_card_effect(current_player, hand)
        else:
            print("Колода пуста!")

    def apply_card_effect(self, player: Player, card: Card):
        card_type = card.typec
        value = card.value
        if card_type == 'vegetable':
            self.move_to_nearest_vegetable(player, value)
        elif card_type == 'sleep':
            print(f"{player} пропускает ход.")
        elif card_type == 'go':
            self.move_forward(player, int(value))
        elif card_type == 'go_last':
            self.move_slowest_forward(int(value))

    def move_to_nearest_vegetable(self, player: Player, vegetable):
        current_position = player.position
        vegetable = self.field.field[current_position]
        current_position = self.go_to_vegetable(vegetable, start=current_position)
        player.goto(current_position)

    def move_forward(self, player, steps):
        current_position = self.player_positions[player]
        new_position = min(current_position + steps, len(self.field.field) - 1)
        # TODO пихать других улиточек вперед
        self.player_positions[player] = new_position
        print(f"{player} двигается вперед на {steps} клеток")

    def move_slowest_forward(self, player, steps):
        sorted_players = sorted(self.player_positions, key=lambda x: self.player_positions[x])
        slowest_player = sorted_players[0]
        self.move_forward(slowest_player, steps)

    def check_end_of_game_condition(self):
        """ Проверяет, что остался 1 активный (возвращает его) или спихнули всех return None"""

        def check_end_of_game_condition(self):
            active_players = [player for player in self.players if player.active]
            if len(active_players) == 1:
                return active_players[0]  # Возвращаем активного игрока, если остался только один
            elif len(active_players) == 0:
                return None  # Никто не остался на поле, игра завершилась
            else:
                return False  # Игра продолжается, более чем один активный игрок на поле
