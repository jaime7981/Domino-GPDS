from classes.domino import Domino
import random

class Board():
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
    
    def start(self):
        if len(self.players) < 1:
            raise Exception("Not enough players")
        
        while len(self.domino_stack) // len(self.players) >= 1:
            for player in self.players:
                player.draw_domino(self.domino_stack.pop())

    def __str__(self) -> str:
        return f"{self.placed_dominos}"