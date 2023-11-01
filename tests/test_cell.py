import unittest
from game.cell import Cell
from game.models import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.multiplier_type,'letter')
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        cell.add_letter(tile=letter,row=0,col=0)
        self.assertEqual(cell.tile, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(tile=letter,row=0,col=0)
        self.assertEqual(cell.calculate_value(),6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(tile=letter,row=0,col=0)
        self.assertEqual(cell.calculate_value(),3)

    # def test_repr_(self):
    #     cell = Cell(tile=Tile('A',1),multiplier=None,multiplier_type='',row=0,col=0)
    #     expected_repr = "Cell(tile=('A',1)-multiplier=None-multiplier_type=-row=0-col=0)"
    #     self.assertEqual(repr(cell), expected_repr)


