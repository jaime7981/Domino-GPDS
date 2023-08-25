from classes.domino import Domino
from classes.player import Player
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

    def player_place_domino(self, player, domino, place):
        if self.is_player_able_to_place_domino(domino)[0]:
            if place == 0:
                self.placed_dominos.insert(0, domino)
            elif place == -1:
                self.placed_dominos.append(domino)
            player.remove_domino(domino)

            return True
        else:
            raise Exception("Player is not able to place domino")
            return False

    def is_player_able_to_place_domino(self, domino):
        if len(self.placed_dominos) == 0:
            return (True,0,False)
        elif domino.values[0] == self.placed_dominos[0].values[0]:
            return (True,0,True)
        elif domino.values[1] == self.placed_dominos[0].values[0]:
            return (True,0,False)
        elif domino.values[0] == self.placed_dominos[-1].values[1]:
            return (True,-1,False)
        elif domino.values[1] == self.placed_dominos[-1].values[1]:
            return (True,-1,True)
        else:
            return (False,None,None)
        
    def select_player_domino(self, player):
        for domino in player.dominos:
            if self.is_player_able_to_place_domino(domino)[0]:
                return (domino, self.is_player_able_to_place_domino(domino))
        
        return None
        
    def is_game_over(self):
        # check if player runs out of dominos
        for player in self.players:
            if len(player.dominos) == 0:
                return [True, player]
    
        # check if no players can place dominos
        for player in self.players:
            for domino in player.dominos:
                if self.is_player_able_to_place_domino(domino)[0]:
                    return [False, None]
           
        return [True, None]
    
    def next_player(self, index_current_player):
        if index_current_player == len(self.players) - 1:
            return self.players[0]
        else:
            return self.players[index_current_player + 1]
            
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
        current_player = starting_player

        self.player_place_domino(current_player, current_player.higher_double_domino(), 0)
        return self.next_player(self.players.index(current_player))

    def next_turn(self, current_player):
        input("Press enter to continue...")
        if self.is_game_over()[0]:
            print(f"Game over!")
            return False
        else:
            if current_player.dominos:
                data_domino = self.select_player_domino(current_player)
                if data_domino is not None:
                    domino = data_domino[0]
                    place = data_domino[1][1]
                    flip = data_domino[1][2]
                    if flip:
                        domino.flip_domino()
                    self.player_place_domino(current_player, domino, place)
                    print(f"{current_player.name} placed {domino} at {place}")
                    return self.next_player(self.players.index(current_player))
                else:
                    print(f"{current_player.name} has no dominos to place!")
                    return self.next_player(self.players.index(current_player))
                #     if flip:
                #         domino.flip_domino()
                #     self.player_place_domino(current_player, domino, place)
                #     print(f"{current_player.name} placed {domino} at {place}")
                #     print(self)
                #     return self.next_player(self.players.index(current_player))
                # else:
                #     print(f"{current_player.name} has no dominos to place!")
                #     return self.next_player(self.players.index(current_player))
                
            else:
                print(f"{current_player.name} has no more dominos!")
                return False

    def set_player(self):
        amount_players = int(input("How many players? "))
        if amount_players < 2:
            print("Not enough players")
            return False
        elif amount_players > 14:
            print("Too many players")
            return False
        for i in range(amount_players):
            self.add_player(Player(f"Player {i + 1} "))
        return True

        
    
    def __str__(self) -> str:
        placed_dominos = ""

        for domino in self.placed_dominos:
            placed_dominos += str(domino) + " "

        return f"{placed_dominos}"