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
    # Utilizar un diccionario para contar las letras en la mano del jugador
        player_letter_count = {}
        for letter in player_tiles:
            player_letter_count[letter] = player_letter_count.get(letter, 0) + 1
    # Transformar las tiles en letras y contar las letras necesarias
        word_letter_count = {}
        for tile in tiles:
            letter = tile.letter
            word_letter_count[letter] = word_letter_count.get(letter, 0) + 1
        # Comparar las letras necesarias con las letras en la mano del jugador
        for letter, quantity in word_letter_count.items():
            if letter not in player_letter_count or player_letter_count[letter] < quantity:
                return False
        return True
    
    def remove_letters_from_hand(self, word):
        for letter in word:
            for tile in self.tiles:
                if tile == letter:
                    self.tiles.remove(tile)
                    break
    
    def exchange_tiles(self, bag, tiles_to_exchange):
        exchanged_tiles = [self.tiles[index] for index in tiles_to_exchange]
        for index in sorted(tiles_to_exchange, reverse=True):
            del self.tiles[index]
        new_tiles = bag.take(len(exchanged_tiles))
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
    

