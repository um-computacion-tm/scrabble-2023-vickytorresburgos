from game.models import BagTiles,Tile
from collections import Counter
from game.board import Board 

class NotEnoughTilesException(Exception):
    pass

class Player:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.tiles = []

    def get_tiles(self, bag: BagTiles, amount):
        self.tiles.extend(bag.take(amount))

    def show_tiles(self):
        return self.tiles
    
    def has_letters(self, tiles=[]):
        player_tiles = [tile.letter for tile in self.tiles]
        # Transform tiles into letters
        word_tiles = [tile.letter for tile in tiles]
        # convert into counter to count needed letters
        needed_tiles = Counter(word_tiles)
        # Compare with the letters available to the player
        for letter, quantity in needed_tiles.items():
            if player_tiles.count(letter) < quantity:
                return False
        return True
    
    def remove_letters_from_hand(self, word):
        for letter in word:
            for tile in self.tiles:
                if tile == letter:
                    self.tiles.remove(tile)
                    break
    
    def exchange_tiles(self, bag, tiles_to_exchange):
        if len(self.tiles) < tiles_to_exchange: #tiles the player want to exchange
            raise NotEnoughTilesException(f"There is not enough tiles to exchange: ({len(self.tiles)} < {tiles_to_exchange})")
        # takes player tiles
        exchanged_tiles = self.tiles[:tiles_to_exchange]
        self.tiles = self.tiles[tiles_to_exchange:]
        # add new tilees in the bag
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