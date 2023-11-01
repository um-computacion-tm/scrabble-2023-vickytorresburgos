import unittest
from game.scrabble2 import Scrabble2
from game.models import Tile
from game.cell import Cell
from game.board import Board

class TestUtil(unittest.TestCase):
    
    def test_simple(self):
        word = [
            Cell(tile =Tile('C', 1, 4),multiplier=None,multiplier_type=''),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
            Cell(tile =Tile('S', 2, 6),multiplier=None,multiplier_type=''),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
        ]
        value = Scrabble2().calculate_word_value(word,[7,7],'V')
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(tile =Tile('C', 1, 4),multiplier=None,multiplier_type=''),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
            Cell(tile=Tile('S', 2, 6), multiplier=2, multiplier_type='letter'),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
        ]
        value = Scrabble2().calculate_word_value(word,[2,4],'H')
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(tile =Tile('C', 1, 4),multiplier=None,multiplier_type=''),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
            Cell(tile=Tile('S', 2, 6),multiplier=2,multiplier_type='word'),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
        ]
        value = Scrabble2().calculate_word_value(word,[4,8],'H')
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(tile =Tile('C', 1, 4),multiplier=3,multiplier_type='letter'),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
            Cell(tile =Tile('S', 2, 6), multiplier=None,multiplier_type=''),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
            Cell(tile =Tile('S', 2, 6), multiplier=2,multiplier_type='word'),
        ]
        value = Scrabble2().calculate_word_value(word,[1,1],'V')
        self.assertEqual(value, 18)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Cell(tile =Tile('C', 1, 4),multiplier=3,multiplier_type='letter'),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
            Cell(tile=Tile('S', 2, 6), multiplier=None,multiplier_type=''),
            Cell(tile =Tile('A', 1, 12),multiplier=None,multiplier_type=''),
            Cell(tile=Tile('S', 2, 6), multiplier=2,multiplier_type='word'),
        ]
        value0 = Scrabble2().calculate_word_value(word,[1,1],'V')    # Calculates word value with multipliers
        value1 = Scrabble2().calculate_word_value(word,[1,1],'V')    # Calculates word value without multipliers (multipliers deactivated)
        self.assertEqual(value1, 7)

    def test_choose_cell_horizontal(self):
        orientation = "H"
        row = 2
        column = 3
        word = "WORD"
        positions = Scrabble2.choose_cell(orientation, row, column, word)
        expected_positions = [(2, 3), (2, 4), (2, 5), (2, 6)]
        self.assertEqual(positions, expected_positions)

    def test_choose_cell_vertical(self):
        orientation = "V"
        row = 3
        column = 2
        word = "WORD"
        positions = Scrabble2.choose_cell(orientation, row, column, word)
        expected_positions = [(3, 2), (4, 2), (5, 2), (6, 2)]
        self.assertEqual(positions, expected_positions)

    # def test_get_tiles_at_location(self):
    #     board = Board()
    #     word = "FACU"
    #     location = (4, 7)
    #     orientation = "H"
    #     board.grid[4][8].tile = Tile('A', 1, 12)
    #     board.grid[4][10].tile = Tile('U', 1)  
    #     list_tiles = Scrabble2.get_tiles_at_location(word, location, orientation, board)
    #     self.assertEqual(len(list_tiles), 2)
    #     self.assertEqual(list_tiles[0].letter, 'A')
    #     self.assertEqual(list_tiles[1].letter, 'U')

    # def test_tiles_needed_to_form_word(self):
    #     board = Board()
    #     word = "FACU"
    #     location = (4, 7)
    #     orientation = "H"
    #     board.grid[4][8].tile = Tile('A', 1)  # Asigna la ficha directamente al atributo "tile" en lugar de crear una nueva celda
    #     board.grid[4][10].tile = Tile('U', 1)  # Asigna la ficha directamente al atributo "tile" en lugar de crear una nueva celda
    #     # Llama a la función que deseas probar (asegúrate de tener esta función en tu código)
    #     tiles_required = Scrabble2.tiles_needed_to_form_word(word, location, orientation, board)
    #     self.assertEqual(len(tiles_required), 2)
    #     self.assertEqual(tiles_required[0].letter, 'F')
    #     self.assertEqual(tiles_required[1].letter, 'C')
        
if __name__ == '__main__':
    unittest.main()