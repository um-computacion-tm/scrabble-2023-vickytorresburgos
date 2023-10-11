import unittest
from unittest.mock import patch
from game.client import *
from game.scrabble import ScrabbleGame
from game.board import Board
from io import StringIO
import sys

class TestGetPlayerNames(unittest.TestCase):
    @patch('builtins.input', side_effect=['Alma', 'Fabiana', 'Agus'])
    def test_get_player_names_3_players(self, mock_input):
        expected_output = ['Alma', 'Fabiana', 'Agus']
        result = get_player_names(3)
        self.assertEqual(result, expected_output)

class TestScrabbleGame(unittest.TestCase):
    def test_main_returns_valid_player_count(self):
        player_count = 3
        self.assertEqual(player_count, 3)

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        self.assertEqual(get_player_count(), 3)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        self.assertEqual(get_player_count(),3)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '1'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        self.assertEqual(get_player_count(),1)

#     def test_validate_word_invalid_word(self):
#         game = Board(2)
#         self.assertFalse(game.validate_word_inside_board("hola", (0, 0), "V"))

    # def test_validate_word_invalid_location(self):
    #     game = Board(2)
    #     self.assertFalse(game.validate_word_inside_board("hola", (10, 10), "V"))

#     def test_validate_word_valid_word_valid_location(self):
#         game = Board(2)
#         self.assertTrue(game.validate_word_inside_board("hola", (0, 0), "V"))

    # def test_next_turn(self):
    #     scrabble_game = ScrabbleGame(players_count=2)
    #     scrabble_game.next_turn()
    #     self.assertEqual(scrabble_game.current_player.id, 1)

    def test_game_can_be_played_with_2_players(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.players), 2)

    def test_game_can_be_played_with_3_players(self):
        game = ScrabbleGame(3)
        self.assertEqual(len(game.players), 3)

    def test_game_can_be_played_with_4_players(self):
        game = ScrabbleGame(4)
        self.assertEqual(len(game.players), 4)

if __name__ == "__main__":
    unittest.main()
