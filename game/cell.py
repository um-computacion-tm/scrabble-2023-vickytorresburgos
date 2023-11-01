from game.models import Tile

class Cell:
    def __init__(self, multiplier, multiplier_type, tile: Tile = None, row=0, col=0):        
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.multiplier_active = True
        self.tile = tile
        self.row = row
        self.col = col

    # def __repr__(self):
    #     return f'Cell(tile={self.tile}-multiplier={self.multiplier}-multiplier_type={self.multiplier_type}-row={self.row}-col={self.col})'

    def add_letter(self, tile: Tile,row,col):
        self.tile = tile
        self.row = row
        self.col = col

    def calculate_value(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == 'letter':
            value = self.tile.value * self.multiplier
            self.multiplier_type = None
            self.multiplier_active = False
            return value
        else:
            return self.tile.value    

    def calculate_word_value(self, word):
        word_value = 0
        word_multiplier = 1
        for cell in word :
            word_value += cell.calculate_value()  
            if cell.multiplier_type == 'word':
                word_multiplier = cell.multiplier
                cell.multiplier_type = None
                cell.multiplier_active = False
        word_value *= word_multiplier
        return word_value


