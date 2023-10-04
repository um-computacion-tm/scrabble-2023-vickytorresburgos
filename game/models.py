import random
class Tile:
    def __init__(self, letter, value, cant):
        self.letter = letter
        self.value = value
        self.cant = cant

class BagTiles:
    def __init__ (self):
            self.tiles = [
                Tile('A', 1, 12),
                Tile('B', 3, 2),
                Tile('C', 3, 4),
                Tile('CH', 5, 1),
                Tile('D', 2, 5),
                Tile('E', 1, 12),
                Tile('F', 4, 1),
                Tile('G', 2, 2),
                Tile('H', 4, 2),
                Tile('I', 1, 6),
                Tile('J', 8, 1),
                Tile('L', 1, 4),
                Tile('LL', 8, 1),
                Tile('M', 3, 2),
                Tile('N', 1, 5),
                Tile('Ñ', 8, 1),
                Tile('O', 1, 9),
                Tile('P', 3, 2),
                Tile('Q', 5, 1),
                Tile('R', 1, 5),
                Tile('RR', 8, 1),
                Tile('S', 1, 6),
                Tile('T', 1, 4),
                Tile('U', 1, 5),
                Tile('V', 4, 1),
                Tile('X', 8, 1),
                Tile('Y', 4, 1),
                Tile('Z', 10, 1),
            ]
            random.shuffle(self.tiles)    
    
    def take(self, count):
        tiles = []
        for _ in range(count):
              tiles.append (self.tiles.pop(0))
        return tiles
    
    def put(self, tiles):
        self.tiles.extend(tiles)
    
