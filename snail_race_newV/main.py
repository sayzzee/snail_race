import json
from card_newV import NumberCard, VegetableCard
from snail_newV import Snail
from game_newV import SnailRaceGame

if __name__ == "__main__":
    player1 = Snail("Первый")
    player2 = Snail("Второй")
    players_list = [player1, player2]

    game = SnailRaceGame(players_list)

    # game.save_game_to_json('saved_game.json')
    # print("Game state saved.")

    #loaded_game = SnailRaceGame(players_list)
    #loaded_game.load_game_from_json('gameV1.json')
    #print("Game state loaded.")

    winner = None
    while not winner:
        current_player = game.players[game.current_player_index]
        print(f"Ход игрока {current_player.name}")
        current_player.show_hand()
        print(f"Текущая позиция: {current_player.position}")
        game.display_field_with_snails()

        card_to_play = int(input(f"Выберите номер карты для игры (0 or 1): "))
        game.play_card(card_to_play)

        winner = game.check_winner()
        if winner:
            print(f"Победила улитка {winner.name}")
            break

        game.current_player_index = current_player.next_player(game.players, game.current_player_index)
