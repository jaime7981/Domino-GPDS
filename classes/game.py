from classes.domino import Domino
import random

class Game():
    def __init__(self) -> None:
        self.players = []
        self.placed_dominos = []
        self.domino_stack = self.create_domino_stack()

    def create_domino_stack(self):
        domino_stack = []
        for i in range(7):
            for j in range(i, 7):
                domino_stack.append(Domino(i, j))

        random.shuffle(domino_stack)

        return domino_stack

    def add_player(self, player):
        self.players.append(player)

    def starting_player(self):
        starting_player = None

        for player in self.players:
            if starting_player is None:
                starting_player = player
            else:
                starting_player = self.compare_players_domino(starting_player, player)
        
        return starting_player
                    
    def compare_players_domino(self, player1, player2):
        if player1.higher_double_domino() is None and player2.higher_double_domino() is None:
            return None
        elif player1.higher_double_domino() is None:
            return player2
        elif player2.higher_double_domino() is None:
            return player1

        if player1.higher_double_domino().values[0] > player2.higher_double_domino().values[0]:
            return player1
        elif player2.higher_double_domino().values[0] > player1.higher_double_domino().values[0]:
            return player2
        else:
            return None

    def player_place_domino(self, player, domino):
        if self.is_player_able_to_place_domino(domino):
            self.placed_dominos.append(domino)
            player.remove_domino(domino)

            return True
        else:
            raise Exception("Player is not able to place domino")
            return False

    def is_player_able_to_place_domino(self, domino):
        if len(self.placed_dominos) == 0:
            return True
        elif domino.values[0] == self.placed_dominos[0].values[0]:
            return True
        elif domino.values[1] == self.placed_dominos[0].values[0]:
            return True
        elif domino.values[0] == self.placed_dominos[-1].values[1]:
            return True
        elif domino.values[1] == self.placed_dominos[-1].values[1]:
            return True
        else:
            return False
        
    def select_player_domino(self, player, domino):
        for domino in player.dominos:
            if self.is_player_able_to_place_domino(domino):
                return domino
        
        return None
        
    def is_game_over(self):
        # check if no players can place dominos
        for player in self.players:
            for domino in player.dominos:
                if self.is_player_able_to_place_domino(domino):
                    break
            else:
                return [True, None]

        # check if player runs out of dominos
        for player in self.players:
            if len(player.dominos) == 0:
                return [True, player]
        
        return [False, None]
            
    def start(self):
        if len(self.players) < 2:
            raise Exception("Not enough players")
        elif len(self.players) > 14:
            raise Exception("Too many players")
        
        while len(self.domino_stack) // len(self.players) >= 1:
            for player in self.players:
                player.draw_domino(self.domino_stack.pop())
        
        starting_player = self.starting_player()
        
        if starting_player is None:
            raise Exception("No starting player")
        
        self.players.remove(starting_player)
        self.players.insert(0, starting_player)

        self.player_place_domino(self.players[0], self.players[0].higher_double_domino())

    def __str__(self) -> str:
        placed_dominos = ""

        for domino in self.placed_dominos:
            placed_dominos += str(domino) + " "

        return f"{placed_dominos}"