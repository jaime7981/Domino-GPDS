from enums.player_type import PlayerType

class Player():
    def __init__(self, name = 'default name', player_type = PlayerType.COMPUTER) -> None:
        self.name = name
        self.player_type = player_type
        self.dominos = []

    def __str__(self) -> str:
        return f'Name: {self.name}\nPlayer Type: {self.player_type}\nDominos: {self.dominos}'