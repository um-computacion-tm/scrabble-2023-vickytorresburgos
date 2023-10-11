from game.models import Tile

class Cell:
    def __init__(self, multiplier, multiplier_type,letter=None, active = True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.active = active
        self.letter = letter

    def add_letter(self, tile:Tile):
        self.letter = tile

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            value = self.letter.value * self.multiplier
            self.multiplier_type = None
            self.multiplier_active = False
            return value
        else:
            return self.letter.value
    
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


