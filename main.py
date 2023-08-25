from classes.game import Game

from enums.player_type import PlayerType

def main():
    main_game = Game()

    while True:
        if main_game.set_player():
            break
    # numeroJugador = (input("escriba la cantidad de jugadores:    "))
    # while True:
    #     if(numeroJugador.isdigit() == False):
    #         print("error no es un caracter valido")
    #         numeroJugador = input("escriba la cantidad de jugadores valida (no caracteres) :    ")
    #     else:
    #         if(int(numeroJugador) < 2 or int(numeroJugador) > 14):
    #             numeroJugador = input(" escriba una cantidad valida entre 2 y 14:   ")
    #         else:
    #             break
    # for i in range(int(numeroJugador)):
    #     main_game.add_player(Player(f'Player {i+1}'))
    
    # # main_game.add_player(Player('Player 2'))
    # # main_game.add_player(Player('Player 3'))
    # # main_game.add_player(Player('Player 4'))
    # # main_game.add_player(Player('Player 5'))

    next_player = main_game.start()
    
    while(True):
        # Leftover domino pieces
        print(len(main_game.domino_stack))

        for domino in main_game.domino_stack:
            print(domino)

        # Players with their domino pieces
        for player in main_game.players:
            print(player)

        # Board with the domino pieces
        print(main_game)
        print()
        next_player = main_game.next_turn(next_player)
        if not next_player:
            break

if __name__ == '__main__':
    main()
