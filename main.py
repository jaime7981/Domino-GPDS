from classes.game import Game
from classes.player import Player
from enums.player_type import PlayerType

def main():
    main_game = Game()

    main_game.add_player(Player('Player 1', PlayerType.HUMAN))
    main_game.add_player(Player('Player 2'))
    main_game.add_player(Player('Player 3'))
    main_game.add_player(Player('Player 4'))
    main_game.add_player(Player('Player 5'))

    main_game.start()

    # Leftover domino pieces
    print(len(main_game.domino_stack))

    for domino in main_game.domino_stack:
        print(domino)

    # Players with their domino pieces
    for player in main_game.players:
        print(player)

    # Board with the domino pieces
    print(main_game)

if __name__ == '__main__':
    main()
