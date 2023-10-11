# import unittest
# # from game.cell import calculate_word_value
# from game.cell import Cell
# from game.models import Tile

# class TestCalculateWordValue(unittest.TestCase):
#     def test_simple(self):
#         celda = Cell()
#         word = [
#             Cell(letter=Tile('C',1)),
#             Cell(letter=Tile('A',1)),
#             Cell(letter=Tile('S',2)),
#             Cell(letter=Tile('A',1))
#         ]
#         value = calculate_word_value()
#         self.assertEqual(value, 5)
#         self.assertEqual(celda.status, 'Inactive')

#     def test_letter_with_multiplier(self):
#         celda = Cell()
#         word = [
#             Cell(letter=Tile('C',1)),
#             Cell(letter=Tile('A',1)),
#             Cell(letter=Tile('S',2), multiplier=2,multiplier_type='letter'),
#             Cell(letter=Tile('A',1))
#         ]
#         value = calculate_word_value()
#         self.assertEqual(value, 7)
#         self.assertEqual(celda.status, 'Inactive')

#     def test_word_with_multiplier(self):
#         celda = Cell()
#         word = [
#             Cell(letter=Tile('C',1)),
#             Cell(letter=Tile('A',1)),
#             Cell(letter=Tile('S',2), multiplier=2,multiplier_type='word'),
#             Cell(letter=Tile('A',1))
#         ]
#         value = calculate_word_value()
#         self.assertEqual(value, 10)
#         self.assertEqual(celda.status, 'Inactive')

#     def test_letter_and_letter_with_multiplier(self):
#         celda = Cell()
#         word = [
#             Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
#             Cell(letter=Tile('A',1)),
#             Cell(letter=Tile('S',2), multiplier=2,multiplier_type='word'),
#             Cell(letter=Tile('A',1))
#         ]
#         value = calculate_word_value()
#         self.assertEqual(value, 14)
#         self.assertEqual(celda.status, 'Inactive')

#     def test_letter_and_letter_with_multiplier_no_active(self):
#         celda = Cell()
#         word = [
#             Cell(letter=Tile('C',1), multiplier=3, multiplier_type='letter'),
#             Cell(letter=Tile('A',1)),
#             Cell(letter=Tile('S',2), multiplier=2,multiplier_type='word'),
#             Cell(letter=Tile('A',1))
#         ]

#         value = calculate_word_value()
#         self.assertEqual(value, 5)
#         self.assertEqual(celda.status, 'Inactive')

# if __name__ == '__main__':
#     unittest.main()