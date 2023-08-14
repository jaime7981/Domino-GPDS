from enums.player_type import PlayerType

class Player():
    def __init__(self, name = 'default name', player_type = PlayerType.COMPUTER) -> None:
        self.name = name
        self.player_type = player_type
        self.dominos = []

    def draw_domino(self, domino):
        self.dominos.append(domino)

    def remove_domino(self, domino):
        self.dominos.remove(domino)

    def higher_double_domino(self):
        higher_double_domino = None

        for domino in self.dominos:
            if domino.is_double():
                if higher_double_domino == None:
                    higher_double_domino = domino
                else:
                    if domino.values[0] > higher_double_domino.values[0]:
                        higher_double_domino = domino
        
        return higher_double_domino

    def __str__(self) -> str:
        return f'Name: {self.name}\nPlayer Type: {self.player_type}\nDominos: {self.dominos}'