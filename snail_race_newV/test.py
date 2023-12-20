import pytest
from card_newV import VegetableCard, NumberCard
from snail_newV import Snail
from game_newV import SnailRaceGame

# Replace 'your_module_name' with the actual name of the module containing the game classes.

def test_snail_creation():
    snail = Snail("TestSnail")
    assert snail.name == "TestSnail"
    assert snail.position == 0
    assert not snail.sleeping

def test_vegetable_card_creation():
    veggie_card = VegetableCard("Carrot")
    assert veggie_card.veggie == "Carrot"

def test_number_card_creation():
    number_card = NumberCard(3, True)
    assert number_card.number == 3
    assert number_card.arrow

def test_snail_race_game_creation():
    players = [Snail("Snail1"), Snail("Snail2")]
    game = SnailRaceGame(players)

    assert len(game.players) == 2
    assert len(game.deck) == 52
    assert len(game.active_snails) == 2
    assert game.current_player_index == 0

def test_snail_race_game_deck_creation():
    players = [Snail("Snail1"), Snail("Snail2")]
    game = SnailRaceGame(players)

    assert all(isinstance(card, (VegetableCard, NumberCard)) for card in game.deck)

def test_snail_race_game_distribute_cards():
    players = [Snail("Snail1"), Snail("Snail2")]
    game = SnailRaceGame(players)

    assert all(len(player.hand) == 2 for player in game.players)

def test_snail_race_game_next_player():
    players = [Snail("Snail1"), Snail("Snail2")]
    game = SnailRaceGame(players)

    assert game.current_player_index == 0
    game.next_player()
    assert game.current_player_index == 1
    game.next_player()
    assert game.current_player_index == 0

def test_snail_race_game_draw_card():
    players = [Snail("Snail1"), Snail("Snail2")]
    game = SnailRaceGame(players)
    initial_hand_size = len(game.players[0].hand)

    game.draw_card(game.players[0])

    assert len(game.players[0].hand) == initial_hand_size + 1
