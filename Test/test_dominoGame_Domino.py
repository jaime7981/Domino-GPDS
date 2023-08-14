import pytest

from classes.domino import Domino
from classes.example_class import ExampleClass
from classes.game import Game
from classes.player import Player
from enums.player_type import PlayerType

################## DOMINO #######################################
def test_is_double():
    domino_double = Domino(3, 3)
    domino_not_double = Domino(2, 5)

    assert domino_double.is_double() == True
    assert domino_not_double.is_double() == False

def test_str_representation():
    domino = Domino(4, 2)
    assert str(domino) == "[4;2]"

def test_repr_representation():
    domino = Domino(1, 6)
    assert repr(domino) == "[1;6]"

