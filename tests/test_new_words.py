import unittest
from game.models import Tile
from game.board import Board, InValidCrossWordException


class TestNewWords(unittest.TestCase):

    def test_new_words_horizontal(self):
        board = Board()
        word1 = [Tile('Q', 5), Tile('U', 1), Tile('E', 1), Tile('S', 1), Tile('O', 1)]
        board.put_words(word1, [7, 7], 'H')
        word2 = 'AYER'
        words = board.new_words(word2, [6, 10], 'H')
        self.assertEqual(words, ['AYER', 'AS', 'YO'])

    def test_new_words_horizontal_wrong(self):
        board = Board()
        word1 = [Tile('Q', 5), Tile('U', 1), Tile('E', 1), Tile('S', 1), Tile('O', 1)]
        board.put_words(word1, [7, 7], 'H')
        word2 = 'R'
        with self.assertRaises(NoValidCrossWordException):
            board.new_words(word2, [6, 10], 'H')

    def test_new_words_vertical(self):
        board = Board()
        word1 = [Tile('Q', 5), Tile('U', 1), Tile('E', 1), Tile('S', 1), Tile('O', 1)]
        board.put_words(word1, [7, 7], 'V')
        word2 = 'AYER'
        words = board.new_words(word2, [10, 6], 'V')
        self.assertEqual(words, ['AYER', 'AS', 'YO'])

    # def test_new_words_vertical(self):
    #     board = Board()
    #     word1 = [Tile('Q', 5), Tile('U', 1), Tile('E', 1), Tile('S', 1), Tile('O', 1)]
    #     board.put_words(word1, [7, 7], 'V')
    #     word2 = 'AYER'
    #     words = board.discover_cross_word(word2, [9,5 ], 'H')
    #     self.assertEqual(words, ['AYER'])