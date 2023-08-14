from classes.board import Board
from classes.player import Player
from enums.player_type import PlayerType

def main():
    main_board = Board()

    main_board.add_player(Player('Player 1', PlayerType.HUMAN))
    main_board.add_player(Player('Player 2'))
    main_board.add_player(Player('Player 3'))
    main_board.add_player(Player('Player 4'))
    main_board.add_player(Player('Player 5'))

    main_board.start()

    # Leftover domino pieces
    print(len(main_board.domino_stack))

    for domino in main_board.domino_stack:
        print(domino)

    # Players with their domino pieces
    for player in main_board.players:
        print(player)

    # Board with the domino pieces
    print(main_board)

    

if __name__ == '__main__':
    main()
