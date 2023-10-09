# import rich
from game.cell import Cell
from game.dictionary import validate_word

triple_word = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
double_word = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
triple_letter = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
double_letter = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11),
                        (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class OutOfBoardException(Exception):
    pass
class OcuppiedCellException(Exception):
    pass
class NoCenterLetterException(Exception):
    pass
class NoWordConnectedException(Exception):
    pass

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]
        self.add_special_cells()
    
    def cell_multiplier(self,coordinate, multiplier_type, multiplier_value):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier_value

    def add_special_cells(self):
        for coordinate in triple_word:
            self.cell_multiplier(coordinate, "word", 3)
        for coordinate in double_word:
            self.cell_multiplier(coordinate, "word", 2)
        for coordinate in triple_letter:
            self.cell_multiplier(coordinate, "letter", 3)
        for coordinate in double_letter:
            self.cell_multiplier(coordinate, "letter", 2)

    def validate_word_inside_board(self, word, location, orientation):
        len_word = len(word)
        pos_x, pos_y = location
        if (orientation == 'H' and pos_x + len_word > 15) or \
            (orientation == 'V' and pos_y + len_word > 15):
            raise OutOfBoardException("Word out of board")
        return True
            
    def empty_place_word(self, word, location, orientation):
        row, col = location
        row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
        for letter in word:
            if self.grid[row][col].letter is not None:
                return False
            row += row_increment
            col += col_increment
        return True
            
    def put_word_first(self, word, location, orientation):
        center_position = (7, 7)
        if orientation == "H":
            word_positions = [(location[0], location[1] + i) for i in range(len(word))]
        elif orientation == "V":
            word_positions = [(location[0] + i, location[1]) for i in range(len(word))]
        if center_position not in word_positions:
            raise NoCenterLetterException("There is no letter in the center")
        return center_position in word_positions

    def put_words_in_board(self, word, location, orientation):
        self.validate_word_inside_board(word, location, orientation)
        if not self.empty_place_word(word, location, orientation):
            raise OcuppiedCellException('Cell already occupied')
        if orientation == 'H':
            positions = [(location[0], location[1] + i) for i in range(len(word))]
        elif orientation == 'V':
            positions = [(location[0] + i, location[1]) for i in range(len(word))]
        for i, pos in enumerate(positions):
            self.grid[pos[0]][pos[1]] = word[i].letter

    def board_is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
    
    def count_letters(self, word, location):
        rows, columns = location
        count = 0
        for letter in word:
            if self.grid[rows][columns].letter is not None:
                count += 1
            rows, columns = rows + 1, columns
        return count

    def adjacent_cells_occupied(self, row, col, orientation):
        adjacent_cells = []
        if orientation == 'H':
            adjacent_cells = [(row - 1, col), (row + 1, col)]
        elif orientation == 'V':
            adjacent_cells = [(row, col - 1), (row, col + 1)]
        return any(self.grid[row][col].letter is not None for row,col  in adjacent_cells) # Ture if any cell around has a letter

    def word_direction(self, word, location, orientation):
        rows, columns = location
        row_change, col_change = (0, 1) if orientation == 'H' else (1, 0)
        for _ in range(len(word)):
            if self.grid[rows][columns].letter is not None or \
                self.adjacent_cells_occupied(rows, columns, orientation):
                return True
            rows += row_change
            columns += col_change
        return False

    def word_connected(self, word, location, orientation):
        if self.count_letters(word, location) != 0:
            return True
        directions = [(0, 1), (0, -1)] if orientation == 'H' else [(1, 0), (-1, 0)]
        rows, columns = location
        for direction in directions:
            row_change, col_change = direction
            current_row, current_col = rows, columns
            if self.word_direction(word, (current_row, current_col), orientation):
                return True
        raise NoWordConnectedException('Words must be connected')
        
    def valid_word_place_board(self, word, location, orientation):
        rows, cols = len(self.grid), len(self.grid[0])
        length = len(word)
    # Check if there is enough space in the word orientation
        if (orientation == 'H' and location[1] + length > cols) or \
            (orientation == 'V' and location[0] + length > rows):
            return False
        intersections = 0
        is_valid = 0
    #Check the cells where the letters of the word will be placed
        for i in range(length):
            if orientation == 'H':
                cell = self.grid[location[0]][location[1] + i].letter
            else:
                cell = self.grid[location[0] + i][location[1]].letter
            if cell is not None:
                intersections += 1  # Count intersections
                if cell.letter == word[i]:
                    is_valid += 1  # Count matching letters
        if is_valid != 0 and intersections == is_valid:
            return True  # Word can be placed at the specified location and orientation
        else:
            return False  
        
    def show_board(self):
    # columns
        columnas = ' '.join(chr(65 + i) for i in range(15))
    # separate rows
        separador = '-' * (3 * 15)
        board_str = f'   {columnas}\n {separador}\n'
    # Board content
        for i in range(15):
            fila = f'{i + 1:2d}| '
            for j in range(15):
                cell = self.grid[i][j]
                try:
                    letter_to_display = cell.letter.upper()
                except AttributeError:
                    letter_to_display = '-'
                fila += f'{letter_to_display} '
            board_str += f'{fila}\n'
        return board_str
