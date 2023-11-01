from game.bagtiles import BagTiles
from game.tiles import Tile
class NoLetterException(Exception):
    pass
class Player:
    def __init__(self):
        self.name=None
        self.score=0
        self.tiles = []

    def take_tiles_from_the_bagtiles(self,bag:BagTiles,amount):
        self.tiles.extend(bag.take(amount)) 
    def exchange_tile(self, bag:BagTiles,tile):
        for i in range(len(self.tiles)):
            if self.tiles[i] == tile:
                popped = self.tiles.pop(i)
                bag.put([popped])
                break
        bag.shuffle_bag()
        self.tiles.extend(bag.take(1))       
    def find_letter_in_tiles(self, letter): #Encontrar letra en tiles
        for tile in self.tiles:
            if tile.get_letter() == letter.upper():
                return tile.get_letter()
        return None  
    def give_requested_tiles(self, word): #verificar q con las tiles formas la palabra
        letters = []
        for letter in word:
            tile = self.find_letter_in_tiles(letter)
            if tile is not None:
                letters.append(tile)
            else:
                raise NoLetterException(f"Letter '{letter}' not found in player's tiles")
        return letters
    def show_tiles(self):
        return self.tiles
    def get_score(self):
        return self.score
    def get_tiles(self):
        return self.tiles
    def get_name(self):
        return self.name  
    def set_name(self,name):
        self.name=name
    def has_letters_str(self, tiles_group, match): 
        tiles_group = tiles_group.upper()
        for i in self.tiles:
            if i.letter in match:
                match[i.letter] += 1
            else:
                match[i.letter] = 1 
        for j in tiles_group:
            if j in match and match[j] >= 1:
                match[j] -= 1
            else:
                return False
        return True 
    def has_letters_list(self, tiles_group, match): 
        for i in tiles_group:
            tiles_group = [letter.upper() for letter in tiles_group]
        for i in self.tiles:
            if i.letter in match:
                match[i.letter] += 1
            else:
                match[i.letter] = 1 
        for j in tiles_group:
            if j in match and match[j] >= 1:
                match[j] -= 1
            else:
                return False
        return True   
    def has_letters_tile(self, tiles_group, match):
        for i in self.tiles:
            if i.letter in match:
                match[i.letter] += 1
            else:
                match[i.letter] = 1 
        for j in tiles_group:
            if j.letter in match and match[j.letter] >= 1:
                match[j.letter] -= 1
            else:
                return False
            
        return True
    def has_letters(self, tiles_group):
        match = {}    
        if isinstance(tiles_group, str):    
            return self.has_letters_str(tiles_group, match)      
        else:       
            if all(isinstance(item, str) for item in tiles_group):
                return self.has_letters_list(tiles_group, match)
            else:
                return self.has_letters_tile(tiles_group, match)  
     
    def remove_tile(self, tile:Tile):
        for i in self.tiles:
            if i.letter == tile.letter:
                self.tiles.remove(i)
                break           
            
    def add_tile(self, tile:Tile):
        self.tiles.append(tile)     