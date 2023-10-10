import unittest
from game.board import Board, OcuppiedCellException, OutOfBoardException, NoCenterLetterException, NoWordConnectedException
from game.models import Tile
from game.cell import Cell
from game.dictionary import validate_word
from unittest.mock import patch

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_board_cell_0_0(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[0][0].multiplier,3 )
        self.assertEqual(cell[0][0].multiplier_type,'word' )

    def test_board_cell_2_6(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[2][6].multiplier,2 )
        self.assertEqual(cell[2][6].multiplier_type,'letter' )

    def test_word_inside_board_h(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True

    def test_word_inside_board_v(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True

    def test_word_out_of_board_v(self):
        board = Board()
        word = "Facultad"
        location = (4, 14)
        orientation = "V"
        with self.assertRaises(OutOfBoardException):
            board.validate_word_inside_board(word,location,orientation)

    def test_word_out_of_board_h(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"
        with self.assertRaises(OutOfBoardException):
            board.validate_word_inside_board(word,location,orientation)

    def test_put_words_in_board_horizontal(self):
        board = Board()
        location = [4, 4]
        orientation = 'H'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        self.assertEqual(board.grid[4][4], word[0].letter)
        self.assertEqual(board.grid[4][5], word[1].letter)
        self.assertEqual(board.grid[4][6], word[2].letter)

    def test_put_words_in_board_horizontal_raises_exception_if_cell_is_occupied(self):
        board = Board()
        board.grid[4][4] = Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type='')
        location = [4, 4]
        orientation = 'H'
        word = [
            Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        ]
        # Try to put the word on the board
        with self.assertRaises(OcuppiedCellException):
            board.put_words_in_board(word, location, orientation)

    def test_put_words_in_board_vertical(self):
        board = Board()
        location = [4, 4]
        orientation = 'V'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        self.assertEqual(board.grid[4][4], word[0].letter)
        self.assertEqual(board.grid[5][4], word[1].letter)
        self.assertEqual(board.grid[6][4], word[2].letter)

    def test_put_words_in_board_vertical_raises_exception_if_cell_is_occupied(self):
        board = Board()
        board.grid[4][4] = Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type='')
        location = [4, 4]
        orientation = 'V'
        word = [
            Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('A', 1,12)),multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        ]
        # Try to put the word on the board
        with self.assertRaises(OcuppiedCellException):
            board.put_words_in_board(word, location, orientation)

    def test_put_word_first_player_h(self):
        board = Board()
        word = 'casa'
        location = (7,6)
        board.put_word_first(word,location, "H")

    def test_put_word_first_player_exception_h(self):
        board = Board()
        word = 'casa'
        location = (4,4)
        with self.assertRaises(NoCenterLetterException):
            board.put_word_first(word,location, "H")   

    def test_put_word_first_player_v(self):
        board = Board()
        word = 'casa'
        location = (5,2)
        with self.assertRaises(NoCenterLetterException):
            board.put_word_first(word,location, "V")
        
    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.board_is_empty(), True)

    def test_empty_place_word_vertical(self):
        board = Board()
        board.empty_place_word('casa',(0, 0), "V")
    
    def test_empty_place_word_horizontal(self):
        board = Board()
        board.empty_place_word('casa',(0, 0), "H")
    
    def test_no_empty_place_word_horizontal(self):
        board = Board()
        board.grid[0][0].letter = Cell(letter=(Tile('R', 1,5)), multiplier=None, multiplier_type='')
        board_is_empty = board.empty_place_word('casa', (0, 0), 'H')
        self.assertFalse(board_is_empty)

    def test_board_is_not_empty_h(self):
        board = Board()
        location = [7,7]
        orientation = 'H'
        word = [
            Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('A', 1,12)),multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word,location,orientation)
        self.assertFalse(board.board_is_empty())

    def test_board_is_not_empty_v(self):
        board = Board()
        location = [7,7]
        orientation = 'V'
        word = [
            Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('A', 1,12)),multiplier=None, multiplier_type=''),
            Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word,location,orientation)
        self.assertFalse(board.board_is_empty())

    def test_word_is_connected_h(self):
        board = Board()
        location = [4, 4]
        orientation = 'H'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        is_connected= board.word_connected('A',[4,7],'H')
        self.assertTrue(is_connected)

    def test_word_is_not_connected_h(self):
        board = Board()
        location = [4, 4]
        orientation = 'H'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        with self.assertRaises(NoWordConnectedException):
            board.word_connected('S',[7,8],'H')

    def test_word_is_connected_up_and_down(self):
        board = Board()
        location = [4, 4]
        orientation = 'H'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        is_connected= board.word_connected('I',[5,4],'H')
        is_connected_1= board.word_connected('Y',[3,7],'H')
        self.assertTrue(is_connected)
        self.assertTrue(is_connected_1)

    def test_word_is_connected_v(self):
        board = Board()
        location = [4, 4]
        orientation = 'V'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        is_connected= board.word_connected('A',[7,4],'V')
        self.assertTrue(is_connected)

    def test_word_is_not_connected_v(self):
        board = Board()
        location = [4, 4]
        orientation = 'V'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)),multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        with self.assertRaises(NoWordConnectedException):
            board.word_connected('S',[6,7],'V')

    def test_word_is_connected_sides(self):
        board = Board()
        location = [4, 4]
        orientation = 'V'
        word = [
        Cell(letter=(Tile('M', 3,2)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('S', 2,6)), multiplier=None, multiplier_type=''),
        Cell(letter=(Tile('A', 1,12)), multiplier=None, multiplier_type=''),
        ]
        board.put_words_in_board(word, location, orientation)
        is_connected= board.word_connected('I',[4,5],'V')
        is_connected_1= board.word_connected('Y',[7,3],'V')
        self.assertTrue(is_connected)
        self.assertTrue(is_connected_1)

    def test_validate_word_place_board_vertical(self):
        board=Board()
        'Palabra 1'
        board.grid[7][7].letter = Tile('c',1,4)
        board.grid[7][8].letter = Tile('a',1,12)
        board.grid[7][9].letter = Tile('m',3,2)
        board.grid[7][10].letter = Tile('a',1,12)
        word = 'saca'
        orientation = 'V'
        location = (5,7)
        self.assertTrue(board.valid_word_place_board(word, location, orientation))

    def test_validate_word_place_board_vertical_not_place(self):
        board=Board()
        'Palabra 1'
        board.grid[7][7].letter = Tile('c',1,4)
        board.grid[7][8].letter = Tile('a',1,12)
        board.grid[7][9].letter = Tile('m',3,2)
        board.grid[7][10].letter = Tile('a',1,12)
        word = 'activamente'
        orientation = 'V'
        location = (6,7)
        self.assertFalse(board.valid_word_place_board(word, location, orientation))

    def test_validate_word_place_board_horizontal(self):
        board=Board()
        'Palabra 1'
        board.grid[7][7].letter = Tile('c',1,4)
        board.grid[7][8].letter = Tile('a',1,12)
        board.grid[7][9].letter = Tile('s',2,6)
        board.grid[7][10].letter = Tile('a',1,12)
        word = 'saca'
        orientation = 'H'
        location = (6,7)
        self.assertFalse(board.valid_word_place_board(word, location, orientation))

    def test_validate_word_place_board_valid(self):
        board=Board()
        board.grid[7][7].add_letter = Tile('c',1,4)
        word = 'saca'
        location = (7,6)
        orientation = 'H'
        self.assertFalse(board.valid_word_place_board(word, location, orientation))

    def test_validate_word_place_board_cross(self):
        board=Board()
        'Palabra 1'
        board.grid[7][7].letter = Tile('c',1,4)
        board.grid[8][7].letter = Tile('a',1,12)
        board.grid[9][7].letter = Tile('m',3,2)
        board.grid[10][7].letter = Tile('a',1,12)
        word = 'saca'
        orientation = 'H'
        location = (8,6)
        self.assertTrue(board.valid_word_place_board(word, location, orientation))

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        self.assertFalse(board.valid_word_place_board(word, location, orientation))

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1,4))
        board.grid[8][7].add_letter(Tile('A', 1,12))
        board.grid[9][7].add_letter(Tile('S', 1,6)) 
        board.grid[10][7].add_letter(Tile('A', 1,12)) 
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.valid_word_place_board(word, location, orientation)
        self.assertLessEqual (word_is_valid , True)

    def test_validate_word_place_board_vertical_not_place(self):
        board=Board()
        'Palabra 1'
        board.grid[7][7].add_letter(Tile('C', 1,4))
        board.grid[8][7].add_letter(Tile('A', 1,12)) 
        board.grid[9][7].add_letter(Tile('S', 1,6)) 
        board.grid[10][7].add_letter(Tile('A', 1,12)) 
        word = 'activamente'
        orientation = 'H'
        location = (6,7)
        self.assertFalse(board.valid_word_place_board(word, location, orientation))

    def test_show_board(self):
        board = Board()
        letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        for i in range(min(len(letras), 15)):
            fila = i // 15
            columna = i % 15
            board.grid[fila][columna].letter = letras[i]
        board_str = board.show_board()
        self.assertEqual(len(board.grid), 15)  # Verify 15 rows
        self.assertEqual(len(board.grid[0]), 15)  # Verify 15 columns

    def test_show_boardd(self):
        board = Board()
        expected_board_str = (
            "   A B C D E F G H I J K L M N O\n"
            ' ---------------------------------------------\n'
            " 1| - - - - - - - - - - - - - - - \n"
            " 2| - - - - - - - - - - - - - - - \n"
            " 3| - - - - - - - - - - - - - - - \n"
            " 4| - - - - - - - - - - - - - - - \n"
            " 5| - - - - - - - - - - - - - - - \n"
            " 6| - - - - - - - - - - - - - - - \n"
            " 7| - - - - - - - - - - - - - - - \n"
            " 8| - - - - - - - - - - - - - - - \n"
            " 9| - - - - - - - - - - - - - - - \n"
            "10| - - - - - - - - - - - - - - - \n"
            "11| - - - - - - - - - - - - - - - \n"
            "12| - - - - - - - - - - - - - - - \n"
            "13| - - - - - - - - - - - - - - - \n"
            "14| - - - - - - - - - - - - - - - \n"
            "15| - - - - - - - - - - - - - - - \n"
        )
        result_board_str = board.show_board()
        self.maxDiff = None
        self.assertEqual(result_board_str, expected_board_str)

    # def test_show_board_with_word(self):
    #     board = Board()
    #     location = (7,7)
    #     orientation = 'H'
    #     word = [
    #         Cell(letter=(Tile('M', 3)), multiplier=None, multiplier_type=''),
    #         Cell(letter=(Tile('A', 1)), multiplier=None, multiplier_type=''),
    #         Cell(letter=(Tile('S', 2)), multiplier=None, multiplier_type=''),
    #     ]
    #     board.put_words_in_board(word,location,orientation)
    #     # Verifica que la palabra se imprime en el tablero
    #     actual_board = board.show_board()
    #     self.assertIn('MAS', actual_board)

if __name__ == '__main__':
    unittest.main()
