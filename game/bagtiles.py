import random
from game.tiles import Tile
TILES = [
    {"letter": "A", "value": 1, "quantity": 12},
    {"letter": "B", "value": 3, "quantity": 2},
    {"letter": "C", "value": 3, "quantity": 4},
    {"letter": "CH", "value": 5, "quantity": 1},
    {"letter": "D", "value": 2, "quantity": 5},
    {"letter": "E", "value": 1, "quantity": 12},
    {"letter": "F", "value": 4, "quantity": 1},
    {"letter": "G", "value": 2, "quantity": 2},
    {"letter": "H", "value": 4, "quantity": 2},
    {"letter": "I", "value": 1, "quantity": 6},
    {"letter": "J", "value": 8, "quantity": 1},
    {"letter": "L", "value": 1, "quantity": 4},
    {"letter": "LL", "value": 8, "quantity": 1},
    {"letter": "M", "value": 3, "quantity": 2},
    {"letter": "N", "value": 1, "quantity": 5},
    {"letter": "Ñ", "value": 8, "quantity": 1},
    {"letter": "O", "value": 1, "quantity": 9},
    {"letter": "P", "value": 3, "quantity": 2},
    {"letter": "Q", "value": 5, "quantity": 1},
    {"letter": "R", "value": 1, "quantity": 5},
    {"letter": "RR", "value": 8, "quantity": 1},
    {"letter": "S", "value": 1, "quantity": 6},
    {"letter": "T", "value": 1, "quantity": 4},
    {"letter": "U", "value": 1, "quantity": 5},
    {"letter": "V", "value": 4, "quantity": 1},
    {"letter": "X", "value": 8, "quantity": 1},
    {"letter": "Y", "value": 4, "quantity": 1},
    {"letter": "Z", "value": 10, "quantity": 1},
    {"letter": "?", "value": 0, "quantity": 2}  
]
class BagTiles:
    def __init__(self):
        self.tiles = []
        for i in TILES:
            for j in range(i.get('quantity')):
                self.tiles.append(Tile(i.get("letter"),i.get("value")))
        random.shuffle(self.tiles)
    def shuffle_bag(self):
        random.shuffle(self.tiles)
    def take(self, count):
        tiles = []
        if count > len(self.tiles):
            count = len(self.tiles)
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles
    def put(self, tiles):
        self.tiles.extend(tiles)