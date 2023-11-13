import pytest
from card import Card
from deck import Deck
from ground import Field

def test_card_creation():
    card = Card('vegetable', 0, 'move to nearest vegetable')
    assert card.typec == 'vegetable'
    assert card.value == 0  # Fix the expected value here
    assert card.game_rule == 'move to nearest vegetable'

def test_card_creation_invalid_type():
    with pytest.raises(ValueError):
        Card('invalid_type', 2)

def test_card_creation_invalid_value():
    with pytest.raises(ValueError):
        Card('go', 10)

def test_card_representation():
    card = Card('go', 3, 'go n steps')
    assert repr(card) == 'go:3 - go n steps'

def test_card_create_method():
    card = Card.create()
    assert card.typec in Card.TYPES
    assert card.value in Card.VALUES

def test_all_cards_method():
    all_cards = Card.all_cards()
    assert len(all_cards) == 50

def test_deck_creation():
    deck = Deck(num_players=3)
    assert len(deck.cards) == 50

def test_shuffle_deck():
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle_deck()
    assert deck.cards != original_order
    assert set(deck.cards) == set(original_order)

def test_deal_cards():
    deck = Deck(num_players=2)
    hands = deck.deal_cards()
    assert len(hands) == 2
    assert all(len(hand) == 2 for hand in hands)

def test_draw_card():
    deck = Deck()
    initial_length = len(deck.cards)
    card = deck.draw_card()
    assert len(deck.cards) == initial_length - 1
    assert card is not None


def test_field_creation():
    field = Field()
    assert len(field.field) == 4

def test_field_initialization():
    field = Field()
    assert hasattr(field, 'field'), "Объект Field должен иметь атрибут 'field'"
    assert isinstance(field.field, list), "'field' атрибут должен быть списком"
    assert len(field.field) == 4, "Поле должно иметь 4 строки"

    for row in field.field:
        assert isinstance(row, list), "Каждая строка в поле должна быть списком"
        assert len(row) == 6, "Каждая строка должна содержать 6 элементов"

def test_field_shuffle():
    # Проверка, что строки перемешиваются независимо
    original_field = [['cucumber', 'peas', 'carrot', 'pepper', 'onion', 'tomato'],
                      ['pepper', 'onion', 'cucumber', 'peas', 'tomato', 'carrot'],
                      ['peas', 'tomato', 'pepper', 'carrot', 'cucumber', 'onion'],
                      ['cucumber', 'pepper', 'onion', 'carrot', 'peas', 'tomato']]

    # Создание экземпляра Field и получение его атрибута field
    field = Field()
    shuffled_field = field.field

    # Убедимся, что элементы в каждой строке остаются теми же
    for original_row, shuffled_row in zip(original_field, shuffled_field):
        assert sorted(original_row) == sorted(shuffled_row), "Элементы в каждой строке должны оставаться теми же"