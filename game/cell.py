from game.models import Tile

class Cell:
    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    def calculate_word_value(self,word):
        word_value = 0
        word_multiplier = 1
        for letter in word:
            word_value += letter.calculate_value()
            if letter.multiplier_type == 'word':
                word_multiplier = letter.multiplier
                letter.multiplier_type = None
        word_value *= word_multiplier
        return word_value