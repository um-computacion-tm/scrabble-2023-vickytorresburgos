import unittest
from game.cell import *
from game.tiles import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(None,True,multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(None,True,multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)
    def test_cell_value(self):
        cell = Cell(None,True,multiplier=2, multiplier_type='L')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(None,True,multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )
    def test_repr_with_letter(self):
        cell = Cell(letter=Tile("X",1), state=True, multiplier=1, multiplier_type=None)
        expected = "[ X ]"  
        self.assertEqual(repr(cell), expected)

    def test_repr_with_tile_2_letters(self):
        cell = Cell(letter=Tile("CH",1), state=True ,multiplier=1,multiplier_type=None)
        expected = "[CH ]"  
        self.assertEqual(repr(cell), expected)

    def test_repr_without_letter(self):
        cell = Cell(letter=None, state=True, multiplier=1, multiplier_type=None)
        expected = "[   ]"
        self.assertEqual(repr(cell), expected)

    def test_repr_with_multiplier(self):
        cell = Cell(letter=None, state=True, multiplier=2, multiplier_type="letter")
        expected = "[letterx2]"
        self.assertEqual(repr(cell), expected)
    def test_has_tile(self):
        cell = Cell(letter=None , state=True , multiplier=1, multiplier_type="")
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        
        validation = cell.has_tile()
        
        self.assertEqual(validation, True)
    def test_get_letter(self):
        cell = Cell(letter=None, state=True, multiplier=1, multiplier_type="")
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter)
        tile = cell.get_tile()
        self.assertEqual(tile.letter,"p")
        self.assertEqual(tile.value,3)
    def test_activate_cell(self):
        cell = Cell(letter=None, state=False, multiplier=2, multiplier_type="W")
        cell.activate_cell()
        self.assertEqual(cell.state,True)
    
    def test_deactivate_cell(self):
        cell = Cell(letter=None, state=True, multiplier=2, multiplier_type="W")
        cell.deactivate_cell()
        self.assertEqual(cell.state,False)    

if __name__ == '__main__':
    unittest.main()