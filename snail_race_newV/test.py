import pytest
from snail_newV import Snail
from card_newV import VegetableCard, NumberCard
from game_newV import SnailRaceGame

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
    assert len(game.deck) == 52  # Assuming default deck configuration
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

def test_snail_race_game_play_card():
    players = [Snail("Snail1"), Snail("Snail2")]
    game = SnailRaceGame(players)
    initial_position = game.players[0].position

    game.play_card(0)

    assert game.players[0].position != initial_position

if __name__ == "__main__":
    pytest.main()
