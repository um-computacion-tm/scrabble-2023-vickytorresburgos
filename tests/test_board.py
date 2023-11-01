import unittest
from game.board import Board, OcuppiedCellException, OutOfBoardException, NoCenterLetterException, NoWordConnectedException
from game.models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),15)
        self.assertEqual(
            len(board.grid[0]),15,)

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
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
        board.put_words(word, (4,4),'H')
        self.assertEqual(board.grid[4][4].tile, tile1) #para que 'H' sea igual a 'H'
        self.assertEqual(board.grid[4][5].tile, tile2)
        self.assertEqual(board.grid[4][6].tile, tile3)

    def test_put_words_horizontal_exception(self):
        board = Board()
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
    # Puts the word
        board.put_words(word, (4,4),'H')
    # Try to put a letter
        self.assertFalse(board.put_words('A', (4,4),'H')) #no la pone

    def test_put_words_in_board_vertical(self):
        board = Board()
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
        board.put_words(word, [4,4],'V')
        self.assertEqual(board.grid[4][4].tile, tile1) #para que 'H' sea igual a 'H'
        self.assertEqual(board.grid[5][4].tile, tile2)
        self.assertEqual(board.grid[6][4].tile, tile3)

    def test_put_words_in_board_vertical_exception(self):
        board = Board()
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
    # Puts the word
        board.put_words(word, [4,4],'H')
    # Try to put a letter
        self.assertFalse(board.put_words('A', (4,4),'H'))


    def test_put_word_first_player_h(self):
        board = Board()
        tile1 = Tile('C',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        location = (7,6)
        self.assertTrue(board.put_word_first_time(word,location, "H"))

    def test_put_word_first_player_exception_h(self):
        board = Board()
        tile1 = Tile('C',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        location = (4,4)
        with self.assertRaises(NoCenterLetterException):
            board.put_word_first_time(word,location, "H")   

    def test_put_word_first_player_v(self):
        board = Board()
        tile1 = Tile('C',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        location = (5,2)
        with self.assertRaises(NoCenterLetterException):
            board.put_word_first_time(word,location, "V")

    def test_valid_update(self):
        board = Board()
        row = 0
        col = 0
        letter = 'A'
        board.update_cell(row, col, letter)
        self.assertEqual(board.grid[row][col].tile.letter, letter)

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.board_is_empty(), True)

    # def test_empty_place_word_vertical(self):
    #     board = Board()
    #     board.empty_place_word('casa',(0, 0), "V")
    
    # def test_empty_place_word_horizontal(self):
    #     board = Board()
    #     board.empty_place_word('casa',(0, 0), "H")
    
    # def test_no_empty_place_word_horizontal(self):
    #     board = Board()
    #     board.grid[0][0].letter = Cell(letter=(Tile('R', 1,5)), multiplier=None, multiplier_type='')
    #     board_is_empty = board.empty_place_word('casa', (0, 0), 'H')
    #     self.assertFalse(board_is_empty)

    def test_board_is_not_empty_h(self):
        board = Board()
        location = [7,7]
        orientation = 'H'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        word = [tile1, tile2, tile3]
        board.put_words(word,location,orientation)
        self.assertFalse(board.is_empty())

    def test_board_is_not_empty_v(self):
        board = Board()
        location = [7,7]
        orientation = 'V'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        word = [tile1, tile2, tile3]
        board.put_words(word,location,orientation)
        self.assertFalse(board.is_empty())

    def test_word_is_connected_h(self):
        board = Board()
        location = [4, 4]
        orientation = 'H'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        board.put_words(word, location, orientation)
        is_connected= board.is_word_connected('A',[4,7],'H')
        self.assertTrue(is_connected)

    def test_word_is_not_connected_h(self):
        board = Board()
        location = [4, 4]
        orientation = 'H'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        board.put_words(word, location, orientation)
        with self.assertRaises(NoWordConnectedException):
            tile0 = Tile('S',1).letter
            board.is_word_connected(tile0,[7,8],'H')

    def test_word_is_connected_up_and_down(self):
        board = Board()
        location = [4, 4]
        orientation = 'H'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        board.put_words(word, location, orientation)
        is_connected= board.is_word_connected('I',[5,4],'H')
        is_connected_1= board.is_word_connected('Y',[3,7],'H')
        self.assertTrue(is_connected)
        self.assertTrue(is_connected_1)

    def test_word_is_connected_v(self):
        board = Board()
        location = [4, 4]
        orientation = 'V'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        board.put_words(word, location, orientation)
        is_connected= board.is_word_connected('A',[7,4],'V')
        self.assertTrue(is_connected)

    def test_word_is_not_connected_v(self):
        board = Board()
        location = [4, 4]
        orientation = 'V'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        board.put_words(word, location, orientation)
        with self.assertRaises(NoWordConnectedException):
            board.is_word_connected('S',[6,7],'V')

    def test_word_is_connected_sides(self):
        board = Board()
        location = [4, 4]
        orientation = 'V'
        tile1 = Tile('M',3)
        tile2 = Tile('A',1)
        tile3 = Tile('S',1)
        tile4 = Tile('A',1)
        word = [tile1, tile2, tile3,tile4]
        board.put_words(word, location, orientation)
        is_connected= board.is_word_connected('I',[4,5],'V')
        is_connected_1= board.is_word_connected('Y',[7,3],'V')
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
        self.assertFalse(board.valid_word_place_board(word, location, orientation))

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

    # def test_place_word_empty_board_vertical_wrong(self):
    #     board = Board()
    #     word = "Facultad"
    #     location = (2, 4)
    #     orientation = "V"
    #     self.assertFalse(board.valid_word_place_board(word, location, orientation))

    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1),row=7,col=7)
        board.grid[8][7].add_letter(Tile('A', 1),row=8,col=7) 
        board.grid[9][7].add_letter(Tile('S', 1),row=9,col=7) 
        board.grid[10][7].add_letter(Tile('A', 1),row=10,col=7) 
        word = "FACULTAD"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        self.assertEqual (word_is_valid , True)

    def test_validate_word_place_board_vertical_not_place(self):
        board=Board()
        'Palabra 1'
        board.grid[7][7].add_letter(Tile('C', 1),row=7,col=7)
        board.grid[8][7].add_letter(Tile('A', 1),row=8,col=7) 
        board.grid[9][7].add_letter(Tile('S', 1),row=9,col=7) 
        board.grid[10][7].add_letter(Tile('A', 1),row=10,col=7) 
        word = 'ACTIVAMENTE'
        orientation = 'H'
        location = (6,7)
        self.assertFalse(board.validate_word_place_board(word, location, orientation))

    def test_show_board(self):
        board = Board()
        letras = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        for i in range(min(len(letras), 15)):
            fila = i // 15
            columna = i % 15
            board.grid[fila][columna].letter = letras[i]
        board_str = board.show_board()
        self.assertEqual(len(board.grid), 15)  # Verify 15 rows
        self.assertEqual(len(board.grid[0]), 15)  # Verify 15 columns
  
    def test_word_to_cells_horizontal(self):
        board = Board()
        word = "MARTES"
        row = 7
        column = 7
        orientation = "H"
        result = board.word_to_cells(word, row, column, orientation)
        self.assertEqual(len(result), len(word))

    def test_word_to_cells_vertical(self):
        board = Board()
        word = "MARTES"
        row = 7
        column = 7
        orientation = "V"
        result = board.word_to_cells(word, row, column, orientation)
        self.assertEqual(len(result), len(word))

    # def test_secondary_word(self):
    #     board= Board()
    #     board.grid[7][7].tile = Tile('Q',5)
    #     board.grid[7][8].tile = Tile('U',1)
    #     board.grid[7][9].tile = Tile('E',1)
    #     board.grid[7][10].tile = Tile('S',1)
    #     board.grid[7][11].tile = Tile('O',1)
if __name__ == '__main__':
    unittest.main()


