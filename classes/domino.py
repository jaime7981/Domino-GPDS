
class Domino():
    def __init__(self, first_value = 0, second_value = 0) -> None:
        self.values = [first_value, second_value]

    def __str__(self) -> str:
        return f"[{self.values[0]}:{self.values[1]}]"