from game.board import Board
from game.board import Player
from game.models import BagTiles

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        for _ in range(players_count):
            self.players.append(Player())
