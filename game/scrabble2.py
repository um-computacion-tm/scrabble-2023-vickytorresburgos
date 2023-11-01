from game.models import Tile
from game.cell import Cell
# from game.tools import Tools

import copy

class Scrabble2:

    @staticmethod
    def convert_word_to_tiles(word: str) -> list:
        letter_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
        return [Tile(letter=letter, value=letter_values.get(letter, 0)) for letter in word]

    # @staticmethod
    # def tiles_to_word(tiles:list) -> str:
    #     return ''.join(tile.letter for tile in tiles)

    def calculate_word_value(self, word: list[Cell], start: list, orientation: str) -> int:
        word_value = 0
        word_multiplier = 1
        row, col = start
        row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
        for cell in word:
            if cell.tile is not None:
                letter_value = cell.calculate_value()
                if cell.multiplier_type == 'word':
                    word_multiplier *= cell.multiplier
                    cell.multiplier_active = False 
                    cell.multiplier_type = None
                word_value += letter_value
            row += row_increment
            col += col_increment
        word_value *= word_multiplier
        return word_value
    
    @staticmethod
    def choose_cell(orientation, row, column,word):
        if orientation == "H":
            positions = [(row, column + i) for i in range(len(word))]
        elif orientation == "V":
            positions = [(row + i, column) for i in range(len(word))]
        return positions

    # @staticmethod
    # def tiles_needed_to_form_word(word, location, orientation, board):
    #     tiles_required = []
    #     word_tiles = scrabble2.convert_word_to_tiles(word)
    #     position_tiles = scrabble2().get_tiles_at_location(word, location, orientation, board)
    #     position_set = set(tile.letter for tile in position_tiles)
    #     for tile in word_tiles:
    #         if tile.letter not in position_set:
    #             tiles_required.append(tile)
    #     print('tiles required: ',tiles_required)
    #     return tiles_required

    # @staticmethod
    # def get_tiles_at_location(word, location, orientation, board):
    #     row, col = location
    #     row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
    #     tiles = []
    #     for letter in word:
    #         cell = board.grid[row][col]  # Accede a la celda en el tablero proporcionado
    #         if cell.tile is not None:
    #             tiles.append(cell.tile)
    #         row += row_increment
    #         col += col_increment
    #     print('tiles: ',tiles)
    #     return tiles