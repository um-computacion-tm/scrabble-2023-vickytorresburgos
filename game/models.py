import random
class Tile:
    def __init__(self, letter, value, cant):
        self.letter = letter
        self.value = value
        self.cant = cant

class BagTiles:
  
    def __init__ (self):
        
        self.tiles = [Tile(letter, value, cant) for letter, value, cant in [
            ('A', 1, 12),
            ('B', 3, 2),
            ('C', 3, 4),
            ('CH', 5, 1),
            ('D', 2, 5),
            ('E', 1, 12),
            ('F', 4, 1),
            ('G', 2, 2),
            ('H', 4, 2),
            ('I', 1, 6),
            ('J', 8, 1),
            ('L', 1, 4),
            ('LL', 8, 1),
            ('M', 3, 2),
            ('N', 1, 5),
            ('Ñ', 8, 1),
            ('O', 1, 9),
            ('P', 3, 2),
            ('Q', 5, 1),
            ('R', 1, 5),
            ('RR', 8, 1),
            ('S', 1, 6),
            ('T', 1, 4),
            ('U', 1, 5),
            ('V', 4, 1),
            ('X', 8, 1),
            ('Y', 4, 1),
            ('Z', 10, 1),
        ]]
        
        random.shuffle(self.tiles)
        self.total_tiles = 0
        for tile in self.tiles:
            self.total_tiles += tile.cant 
    
    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        self.total_tiles -= count    
   
    def put(self, tiles):
        self.tiles.extend(tiles)