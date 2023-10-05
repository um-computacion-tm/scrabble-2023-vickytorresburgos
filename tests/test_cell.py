import unittest
from game.cell import Cell
from game.models import Tile

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

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
        cell = Cell(multiplier=1, multiplier_type='', letter=None)
        letter = Tile(letter='p', value=3, cant=2)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3,cant=2)
        cell.add_letter(letter=letter)
        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3, cant=2)
        cell.add_letter(letter=letter)
        self.assertEqual(
            cell.calculate_value(),
            3,
        )

class TestCalculateValue(unittest.TestCase):
    def test_simple(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(letter=Tile('C',1,4),multiplier_type='', multiplier=None),
            Cell(letter=Tile('A',1,12),multiplier_type='', multiplier=None),
            Cell(letter=Tile('S',2,6),multiplier_type='', multiplier=None),
            Cell(letter=Tile('A',1,12),multiplier_type='', multiplier=None)
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(letter=Tile('C',1,4),multiplier_type='', multiplier=None),
            Cell(letter=Tile('A',1,12),multiplier_type='', multiplier=None),
            Cell(letter=Tile('S',2,6),multiplier = 2, multiplier_type ='letter'),
            Cell(letter=Tile('A',1,12),multiplier_type='', multiplier=None),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(letter=Tile('C',1,4),multiplier = None, multiplier_type =''),
            Cell(letter=Tile('A',1,12),multiplier = None, multiplier_type =''),
            Cell(letter=Tile('S',2,6), multiplier = 2, multiplier_type ='word'),
            Cell(letter=Tile('A',1,12),multiplier = None, multiplier_type =''),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(multiplier=3,multiplier_type='letter',letter=Tile('C', 1,4)),
            Cell(letter=Tile('A', 1,12),multiplier = None, multiplier_type =''),
            Cell(letter=Tile('S', 2,6), multiplier=2,multiplier_type='word'),
            Cell(letter=Tile('A', 1,12),multiplier = None, multiplier_type =''),
        ]
        value = cell.calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_active_and_inactive(self):
        cell = Cell(multiplier=None, multiplier_type='')
        word = [
            Cell(multiplier=3, multiplier_type='letter',letter=Tile('C', 1,4)),
            Cell(letter=Tile('A', 1, 12),multiplier = None, multiplier_type =''),
            Cell(letter=Tile('S', 1, 6), multiplier=2,multiplier_type='word'),
            Cell(letter=Tile('A', 1, 12),multiplier = None, multiplier_type =''),
        ]
        value1 = cell.calculate_word_value(word) #active cells
        value2 = cell.calculate_word_value(word) #inactive cells
        self.assertEqual(value1, 12)
        self.assertEqual(value2, 4)


if __name__ == '__main__':
    unittest.main()
