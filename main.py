from classes.game import Game

from enums.player_type import PlayerType

def main():
    main_game = Game()

    while True:
        if main_game.set_players():
            break

    
    next_player = main_game.start()
    # for player in main_game.players:
    #     print(player)
    # print()
    
    while(True):
        # Leftover domino pieces
        main_game.print_staus_game(next_player)

        # for domino in main_game.domino_stack:
        #     print(domino)

        # # Players with their domino pieces
        # for player in main_game.players:
        #     print(player)

        # # Board with the domino pieces
        # print(main_game)
        # print()
        next_player = main_game.next_turn(next_player)
        if not next_player:
            break
    print()
    # Players with their domino pieces
    for player in main_game.players:
        print(player)
    print()
    # Board with the domino pieces
    print(main_game)
    print()

if __name__ == '__main__':
    main()
