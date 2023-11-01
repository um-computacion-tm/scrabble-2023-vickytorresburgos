import copy
from game.cell import Cell
from game.dictionary import validate_word
from colorama import Fore, Back, Style, init
from game.cell import Cell
from game.scrabble2 import Scrabble2


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
class InValidCrosswordException(Exception):
    pass
class NoWordConnectedException(Exception):
    pass

class NoCenterLetterException(Exception):
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
        if self.first_time:
            self.validate_len_word_inside_board(word_list_of_tiles, location, orientation)
            center_position = (7, 7)
            if orientation == "H":
                word_positions = [(location[0], location[1] + i) for i in range(len(word_list_of_tiles))]
            elif orientation == "V":
                word_positions = [(location[0] + i, location[1]) for i in range(len(word_list_of_tiles))]
            if center_position not in word_positions:
                raise NoCenterLetterException("There is no letter in the center")
            self.put_words(word_list_of_tiles, location, orientation)
            self.first_time = False
            print(word_list_of_tiles)
            return True  

    def put_words_in_board(self, word, location, orientation):
        self.validate_len_word_inside_board(word_list_of_tiles, location, orientation)
        len_word = len(word_list_of_tiles)
        row, col = location
        row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
        # Place the tiles on the board
        for i in range(len_word):
            if self.grid[row][col].tile is None:  # checks if cell at current position is empty
                self.grid[row][col].tile = word_list_of_tiles[i]  # If it's empty,it puts a letter
            row += row_increment
            col += col_increment

    def update_cell(self, row, col, letter):
        if 0 <= row < 15 and 0 <= col < 15:
            self.grid[row][col].add_letter(Tile(letter, 1), row, col)


    def board_is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
        
    def word_connected(self, word, location, orientation):
        r, c = location  # Row and column
        count = 0
        adjacent_cells = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for direction in adjacent_cells:
            dr, dc = direction  # Direction of the adjacent cell (dr= dir row) (dc= dir col)
            if 0 <= dr < 15 and 0 <= dc < 15 and self.grid[dr][dc].tile is not None:
                count += 1
            for _ in range(len(word)):
                if orientation == 'H':
                    c += 1
                elif orientation == 'V':
                    r += 1
        if count != 0:
            return True
        else:
            raise NoWordConnectedException('Words must be connected')
        
    def valid_word_place_board(self, word, location, orientation):
        rows, cols = len(self.grid), len(self.grid[0])
        length = len(word)
        if (orientation == 'H' and location[1] + length > cols) or \
            (orientation == 'V' and location[0] + length > rows):
            return False
        intersections = 0
        is_valid = 0
        for i in range(length):
            if orientation == 'H':
                cell = self.grid[location[0]][location[1] + i].tile
            else:
                cell = self.grid[location[0] + i][location[1]].tile
            if cell is not None:
                intersections += 1  # Count intersections
                if cell.letter == word[i]:
                    is_valid += 1  # Count matching letters
        if is_valid != 0 and intersections == is_valid:
            return True  # Word can be placed at the specified location and orientation
        else:
            return False
        
    def show_board(self):
        init()
    # columns
        columnas = ' ' + '  '.join(f'{i:2d}' for i in range(15))  
    # separate rows
        separador = '─' * 65  
        board_str = f'\n   {columnas}\n {separador}\n'
    # Board content
        for i in range(15):
            fila = f'{i:2d}│ '  
            row_cells = []  
            for j in range(15):
                cell = self.grid[i][j]
                try:
                    letter_to_display = cell.tile.letter.upper()
                except AttributeError:
                    letter_to_display = ' '
                background_color = ""
                if (i, j) in triple_word:
                    background_color = Back.RED
                elif (i, j) in double_word:
                    background_color = Back.MAGENTA
                elif (i, j) in triple_letter:
                    background_color = Back.GREEN
                elif (i, j) in double_letter:
                    background_color = Back.BLUE
                cell_text = f'{background_color} {letter_to_display} {Style.RESET_ALL}'  
                row_cells.append(cell_text)
            fila += '│'.join(row_cells) + '│' 
            board_str += f'{fila}\n{separador}\n'  
        board_str += f' {separador} \n'  
        board_str += "Legend:\n"
        board_str += f"{Back.RED}  {Style.RESET_ALL} = x3 Word\n"
        board_str += f"{Back.MAGENTA}  {Style.RESET_ALL} = x2 Word\n"
        board_str += f"{Back.GREEN}  {Style.RESET_ALL} = x3 letter\n"
        board_str += f"{Back.BLUE}  {Style.RESET_ALL} = x2 Letter\n"
        return board_str
    
    def new_words(self, word: str, start: list, orientation: str) -> list:
        original_grid = copy.deepcopy(self.grid)
        tiles = Scrabble2.convert_word_to_tiles(word=word)
        self.put_words(tiles, start, orientation)
        new_words = [word]
        other_orientation = 'V' if orientation == 'H' else 'H'
        cells_to_analyze = self.make_cells_to_analyze(len(tiles), start, orientation)
        for cell in cells_to_analyze:
            cross_word = self.discover_cross_word(cell, other_orientation)
            if len(cross_word) > 1:
                new_words.append(cross_word)
                if not validate_word(cross_word):
                    raise InValidCrosswordException('Cross word must be valid')
        self.grid = copy.deepcopy(original_grid)
        return new_words

    def make_cells_to_analyze(self, size: int, start: list, orientation: str):
        row, col = start
        row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
        cells = []
        for _ in range(size):
            cells.append(self.grid[row][col])
            row += row_increment
            col += col_increment
        return cells

    def discover_cross_word(self, cell: Cell, orientation: str) -> str:
        row_increment, col_increment = (0, -1) if orientation == 'H' else (-1, 0)
        # analyzing before
        row = cell.row
        col = cell.col
        word = ''
        while self.grid[row + row_increment][col + col_increment].tile is not None:
            row += row_increment
            col += col_increment
            word += self.grid[row][col].tile.letter
        # adding letter in cell
        word = word[::-1]
        word += cell.tile.letter
        # analyzing after
        row = cell.row
        col = cell.col
        row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
        while self.grid[row + row_increment][col + col_increment].tile is not None:
            row += row_increment
            col += col_increment
            word += self.grid[row][col].tile.letter
        return word
    
    def word_to_cells(self, word, row, column, orientation):
        list_tiles = Scrabble2().convert_word_to_tiles(word)
        list_cell = []
        for i in range(len(word)):
            tile = list_tiles[i]
            cell_row = row
            cell_column = column
            cell = copy.copy(self.grid[cell_row][cell_column])
            cell.add_letter(tile, cell_row, cell_column)
            list_cell.append(cell)
            if orientation == 'H':
                column += 1  
            elif orientation == 'V':
                row += 1  
        return list_cell

    # def count_letters(self, word, location):
    #     rows, columns = location
    #     count = 0
    #     for letter in word:
    #         if self.grid[rows][columns].letter is not None:
    #             count += 1
    #         rows, columns = rows + 1, columns
    #     return count

    # def adjacent_cells_occupied(self, row, col, orientation):
    #     adjacent_cells = []
    #     if orientation == 'H':
    #         adjacent_cells = [(row - 1, col), (row + 1, col)]
    #     elif orientation == 'V':
    #         adjacent_cells = [(row, col - 1), (row, col + 1)]
    #     return any(self.grid[row][col].letter is not None for row,col  in adjacent_cells) # Ture if any cell around has a letter

    # def word_direction(self, word, location, orientation):
    #     rows, columns = location
    #     row_change, col_change = (0, 1) if orientation == 'H' else (1, 0)
    #     for _ in range(len(word)):
    #         if self.grid[rows][columns].letter is not None or \
    #             self.adjacent_cells_occupied(rows, columns, orientation):
    #             return True
    #         rows += row_change
    #         columns += col_change
    #     return False
                
    # def detect_secondary_word(self, row, col, orientation):
    #     if self.grid[row][col].tile:
    #         # La celda ya contiene una ficha, por lo que no hay una palabra secundaria aquí.
    #         return None
    # # Analizar en la dirección opuesta para formar la palabra secundaria
    #     row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
    #     secondary_word = ''
    #     row -= row_increment
    #     col -= col_increment
    #     while row >= 0 and col >= 0 and self.grid[row][col].tile:
    #     # Revisar celdas en la dirección opuesta y agregar letras a la palabra secundaria.
    #         secondary_word = self.grid[row][col].tile.letter + secondary_word
    #         row -= row_increment
    #         col -= col_increment
    #     if secondary_word:
    #     # Devolver la palabra secundaria detectada y su ubicación
    #         return (secondary_word, [row + row_increment, col + col_increment], 'H' if orientation == 'V' else 'V')
    #     else:
    #         # No se encontró ninguna palabra secundaria.
    #         return None
        
    # def detect_secondary_words(self, word, start, orientation):
    #     secondary_words = []
    #     for i in range(len(word)):
    #         row, col = start[0], start[1]
    #         if orientation == 'H':
    #             col += i
    #         else:
    #             row += i
    #     # Detectar palabra secundaria en dirección opuesta
    #         secondary_word = self.detect_secondary_word(row, col, orientation)
    #         if secondary_word:
    #             secondary_words.append(secondary_word)
    #     return secondary_words





