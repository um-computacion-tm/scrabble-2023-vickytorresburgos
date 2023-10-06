from game.models import BagTiles,Tile
from collections import Counter

class NotEnoughTilesException(Exception):
    pass

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.tiles = []

    def take_tiles(self, bag: BagTiles, amount):
        self.tiles.extend(bag.take(amount))

    def has_letters(self, tiles=[]):
        letras_jugador = [tile.letter for tile in self.tiles]
        letras_palabra = [tile.letter for tile in tiles]
        letras_necesarias = Counter(letras_palabra)
        for letra, cantidad in letras_necesarias.items():
            if letras_jugador.count(letra) < cantidad:
                return False
        return True
    
    def exchange_tiles(self, bag, tiles_to_exchange):
        if len(self.tiles) < tiles_to_exchange:
            raise NotEnoughTilesException(f"No hay suficientes fichas para intercambiar ({len(self.tiles)} < {tiles_to_exchange})")
        exchanged_tiles = self.tiles[:tiles_to_exchange]
        self.tiles = self.tiles[tiles_to_exchange:]
        new_tiles = bag.take(tiles_to_exchange)
        self.tiles.extend(new_tiles)
        return exchanged_tiles, new_tiles
    
    def write_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def increase_score(self,amount):
        self.score += amount

    def get_score(self):
        return self.score