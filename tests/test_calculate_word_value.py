import unittest
from game.cell import *
from game.tiles import Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(Tile('C', 1),True,1,'L'),
            Cell(Tile('A', 1),True,1,'L'),
            Cell(Tile('S', 2),True,1,'L'),
            Cell(Tile('A', 1),True,1,'L'),
        ]
        value = calculate_word_value(word).calculate_word()
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
         word = [
             Cell(Tile('C', 1),True,1,'L'),
             Cell(Tile('A', 1),True,1,'L'),
             Cell(Tile('S', 2),True,2,'L'),
             Cell(Tile('A', 1),True,1,'L')
         ]
         value = calculate_word_value(word).calculate_word()
         self.assertEqual(value, 7 )   
    def test_with_word_multiplier(self):
        word = [
            Cell(Tile('C', 1),True,1,'L'),
            Cell(Tile('A', 1),True,1,'L'),
             Cell(Tile('S', 2),True,2,'W'),
            Cell(Tile('A', 1),True,1,'L')
            
        ]
        value = calculate_word_value(word).calculate_word()
        self.assertEqual(value, 10)
    def test_with_letter_word_multiplier(self):
         word = [
             Cell(Tile('C', 1),True,3,'L'),
             Cell(Tile('A', 1),True,1,'L'),
             Cell(Tile('S', 2),True,2,'W'),
             Cell(Tile('A', 1),True,1,'L')
         ]
         value = calculate_word_value(word).calculate_word()
         self.assertEqual(value, 14)
    def test_with_letter_word_multiplier_no_active(self):
         
         word = [
             Cell(Tile('C', 1),False,3,'L'),
             Cell(Tile('A', 1),True,1,'L'),
             Cell(Tile('S', 2),False,2,'W'),
             Cell(Tile('A', 1),True,1,'L'),
         ]
         value=calculate_word_value(word).calculate_word()
         self.assertEqual(value, 5)

if __name__ == '__main__':
    unittest.main()