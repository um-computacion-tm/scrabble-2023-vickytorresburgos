from game.cell import Cell
class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, "") for _ in range(15)] 
            for _ in range(15)
            ]

    def calculate_word_value(word: list[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value
    
    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        posicion_x = location[0]
        posicion_y = location[1]

        if orientation == 'H':
            if posicion_x + len_word > 15:
                return False
            else:
                return True
        elif orientation == 'V':
            if posicion_y + len_word > 15:
                return False
            else:
                return True