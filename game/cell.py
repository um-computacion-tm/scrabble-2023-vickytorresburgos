from game.tiles import Tile
from game.bagtiles import BagTiles
class Cell:
    def __init__(self,letter,state,multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter=letter
        self.state=state
    def __repr__(self):
        if self.letter != None:
            if self.letter.letter in ("CH", "RR", "LL"):
                return f"[{self.letter.letter} ]"  
            return f"[ {self.letter.letter} ]"    
        else:
            if self.multiplier == 1:
                return f"[   ]"
            else:
                return f"[{self.multiplier_type}x{self.multiplier}]"
    def add_letter(self, letter:Tile):
        self.letter = letter
    def has_tile(self):
        return self.letter is not None   
    def get_tile(self):
        return self.letter
    def activate_cell(self):
        if self.state == False:
            self.state = True
    def deactivate_cell(self):
        if self.state == True:
            self.state = False
    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'L'and self.state==True:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
class calculate_word_value:
    def __init__(self,word) : 
        self.word=word       
    def calculate_word(self):
        values = 0
        for cell in self.word:
            values += cell.calculate_value()
        for cell in self.word:
            if cell.multiplier_type == 'W' and cell.state == True:
                values = values * cell.multiplier

        return values
        
              
        
        