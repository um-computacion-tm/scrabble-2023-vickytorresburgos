import unittest
from game.board import Board
from game.tiles import Tile
from game.cell import Cell
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
    def test_board_cell_00(self):
        board = Board()
        board.add_bonus()
        cell = board.grid
        self.assertEqual(cell[0][0].multiplier,3 )
        self.assertEqual(cell[0][0].multiplier_type,'W' )
    def test_board_cell_33(self):
        board=Board()
        board.add_bonus()
        cell=board.grid
        self.assertEqual(cell[3][3].multiplier,2)
        self.assertEqual(cell[3][3].multiplier_type,'W')
    def test_word_inside_board(self):
         board= Board()
         word = "Facultad"
         location = (5, 4)
         orientation = "H"
         word_is_valid = board.validate_word_inside_board(word, location, orientation)
         assert word_is_valid == True
    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (4, 14)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False
    def test_word_inside_board_vertical(self):
        board = Board()
        word = "FACULTAD"
        location = (5, 4)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
    def test_board_is_empty(self):
        board = Board()
        board.empty()
        assert board.is_empty == True
    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.empty()
        assert board.is_empty == False
    def test_place_word_empty_board_horizontal_fine(self):
         board = Board()
         word = "FACULTAD"
         location = (7, 4)
         orientation = "H"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == True  
    def test_place_word_empty_board_horizontal_wrong(self):
         board = Board()
         word = "FACULTAD"
         location = (2, 4)
         orientation = "H"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == False
    def test_place_word_empty_board_vertical_fine(self):
         board = Board()
         word = "FACULTAD"
         location = (4, 7)
         orientation = "V"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == True  
    def test_place_word_empty_board_vertical_wrong(self):
         board = Board()
         word = "FACULTAD"
         location = (2, 4)
         orientation = "V"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == False
    def test_place_word_not_empty_board_horizontal_fine(self):
         board = Board()
         board.grid[7][7].add_letter(Tile('C', 1))
         board.grid[8][7].add_letter(Tile('A', 1)) 
         board.grid[9][7].add_letter(Tile('S', 1)) 
         board.grid[10][7].add_letter(Tile('A', 1)) 
         word = "FACULTAD"
         location = (8, 6)
         orientation = "H"
         word_is_valid = board.validate_word_place_board(word, location, orientation)
         assert word_is_valid == True  
    def test_place_word_not_empty_board_horizontal_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = "MISA"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
    def test_place_word_not_empty_board_vertical_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = "FACULTAD"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == True
    def test_place_word_not_empty_board_vertical_not_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = "MISA"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False  
    
 
    def test_check_word_left(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = board.check_word_left(row=7, col=11)
        self.assertEqual(word[0].get_tile().get_letter(),'C')
        self.assertEqual(word[1].get_tile().get_letter(),'A')
        self.assertEqual(word[2].get_tile().get_letter(),'S')
        self.assertEqual(word[3].get_tile().get_letter(),'A')
        
    def test_check_word_right(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        word = board.check_word_right(row=7, col=6)
        self.assertEqual(word[0].get_tile().get_letter(),'C')
        self.assertEqual(word[1].get_tile().get_letter(),'A')
        self.assertEqual(word[2].get_tile().get_letter(),'S')
        self.assertEqual(word[3].get_tile().get_letter(),'A')
        
    def test_check_word_up(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = board.check_word_up(row=11, col=7)
        self.assertEqual(word[0].get_tile().get_letter(),'C')
        self.assertEqual(word[1].get_tile().get_letter(),'A')
        self.assertEqual(word[2].get_tile().get_letter(),'S')
        self.assertEqual(word[3].get_tile().get_letter(),'A')
        
    def test_check_word_down(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        word = board.check_word_down(row=6, col=7)
        self.assertEqual(word[0].get_tile().get_letter(),'C')
        self.assertEqual(word[1].get_tile().get_letter(),'A')
        self.assertEqual(word[2].get_tile().get_letter(),'S')
        self.assertEqual(word[3].get_tile().get_letter(),'A')
    
    def test_check_word_horizontal(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][9].add_letter(Tile('S', 1)) 
        board.grid[7][10].add_letter(Tile('A', 1)) 
        board.grid[7][11].add_letter(Tile('D', 1))
        board.grid[7][12].add_letter(Tile('O', 1))
        board.grid[7][13].add_letter(Tile('S', 1))
        word = board.check_word_horizontal(row=7, col=10)
        self.assertEqual(word[0].get_tile().get_letter(),'C')
        self.assertEqual(word[1].get_tile().get_letter(),'A')
        self.assertEqual(word[2].get_tile().get_letter(),'S')
        self.assertEqual(word[3].get_tile().get_letter(),'A')
        self.assertEqual(word[4].get_tile().get_letter(),'D')
        self.assertEqual(word[5].get_tile().get_letter(),'O')
        self.assertEqual(word[6].get_tile().get_letter(),'S')
        
    def test_check_word_horizontal_empty(self):
        board = Board()
        board.grid[7][5].add_letter(Tile('C', 1))
        board.grid[7][6].add_letter(Tile('A', 1)) 
        board.grid[7][7].add_letter(Tile('S', 1)) 
        board.grid[7][8].add_letter(Tile('A', 1)) 
        board.grid[7][10].add_letter(Tile('S', 1)) 
        board.grid[7][12].add_letter(Tile('D', 1))
        board.grid[7][13].add_letter(Tile('O', 1))
        board.grid[7][14].add_letter(Tile('S', 1))
        word = board.check_word_horizontal(row=7, col=10)
        self.assertEqual(word, False)
        
    def test_check_word_vertical(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[9][7].add_letter(Tile('S', 1)) 
        board.grid[10][7].add_letter(Tile('A', 1)) 
        board.grid[11][7].add_letter(Tile('D', 1))
        board.grid[12][7].add_letter(Tile('O', 1))
        board.grid[13][7].add_letter(Tile('S', 1))
        word = board.check_word_vertical(row=10, col=7)
        self.assertEqual(word[0].get_tile().get_letter(),'C')
        self.assertEqual(word[1].get_tile().get_letter(),'A')
        self.assertEqual(word[2].get_tile().get_letter(),'S')
        self.assertEqual(word[3].get_tile().get_letter(),'A')
        self.assertEqual(word[4].get_tile().get_letter(),'D')
        self.assertEqual(word[5].get_tile().get_letter(),'O')
        self.assertEqual(word[6].get_tile().get_letter(),'S')
        
    def test_check_word_vertical_empty(self):
        board = Board()
        board.grid[5][7].add_letter(Tile('C', 1))
        board.grid[6][7].add_letter(Tile('A', 1)) 
        board.grid[7][7].add_letter(Tile('S', 1)) 
        board.grid[8][7].add_letter(Tile('A', 1)) 
        board.grid[10][7].add_letter(Tile('S', 1)) 
        board.grid[12][7].add_letter(Tile('D', 1))
        board.grid[13][7].add_letter(Tile('O', 1))
        board.grid[14][7].add_letter(Tile('S', 1))
        word = board.check_word_vertical(row=10, col=7)
        self.assertEqual(word, False)
    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "FACULTAD"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_place_board(word, location, orientation)
        assert word_is_valid == False
          
if __name__ == '__main__':
    unittest.main()