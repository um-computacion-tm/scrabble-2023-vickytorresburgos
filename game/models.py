import random

class NoTilesInTheBagException(Exception):
    pass

class Tile:
    def __init__(self, letter, value, cant):
        self.letter = letter
        self.value = value
        self.cant = cant
        
    def __repr__(self):
        return f"('{self.letter}',{self.value})"

class JokerTile(Tile):
    def __init__(self, letter, value):
        super().__init__(letter, value)

    def select_letter(self, selection):
        selection = selection.upper()
        for tile in BagTiles:
            if selection == tile['letter']:
                self.letter = tile['letter']
                self.value = 0

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
    
class Tiles:
    def __init__(self):
        self.tiles = []
        for tile_info in BagTiles:
            for _ in range(tile_info["quantity"]):
                letter = tile_info["letter"]
                value = tile_info["value"]
                tile = Tile(letter, value)
                self.tiles.append(tile)
        random.shuffle(self.tiles)

    def __len__(self):
        return len(self.tiles)
    
    def tiles_left_in_bag(self):
        return len(self.tiles)

    def take(self, amount):
        if not self.tiles:
            raise NoTilesInTheBagException("No tiles left in the bag")
        if amount > len(self.tiles):
            amount = len(self.tiles)
        return [self.tiles.pop() for _ in range(amount)]

    def put(self, tiles=list):
        self.tiles.extend(tiles)
    
