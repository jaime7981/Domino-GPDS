import pytest

from classes.domino import Domino
from classes.example_class import ExampleClass
from classes.game import Game
from classes.player import Player
from enums.player_type import PlayerType

############################### PLAYER ############################
def test_initialization():
    player = Player()
    assert player.name == 'default name'
    assert player.player_type == PlayerType.COMPUTER
    assert player.dominos == []

def test_draw_domino():
    player = Player()
    domino = Domino(3, 3)
    player.draw_domino(domino)
    assert len(player.dominos) == 1
    assert player.dominos[0] == domino

def test_remove_domino():
    player = Player()
    domino = Domino(1, 4)
    player.draw_domino(domino)
    player.remove_domino(domino)
    assert len(player.dominos) == 0

def test_higher_double_domino():
    player = Player()
    domino1 = Domino(1, 1)
    domino2 = Domino(3, 3)
    domino3 = Domino(5, 5)
    player.draw_domino(domino1)
    player.draw_domino(domino2)
    player.draw_domino(domino3)
    result = player.higher_double_domino()
    assert result == domino3