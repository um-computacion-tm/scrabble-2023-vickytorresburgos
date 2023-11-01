import unittest
from unittest.mock import patch, call
from game.scrabble_cli import ScrabbleCli
from game.scrabble import ScrabbleGame
from game.board import Board
from io import StringIO
from game.player import Player
from game.models import Tile
import sys
from colorama import Fore, Style, init

class TestScrabbleGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['Victoria', 'Alma', 'Valentina'])
    def test_get_player_names_3_players(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=3)
        expected_output = ['Victoria', 'Alma', 'Valentina']
        result = scrabble_cli.get_player_names(3)
        self.assertEqual(result, expected_output)

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        scrabble_cli = ScrabbleCli(player_count=3)
        self.assertEqual(scrabble_cli.get_player_count(), 3)

    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched):
        scrabble_cli = ScrabbleCli(player_count=3)
        self.assertEqual(scrabble_cli.get_player_count(),3)

    @patch('builtins.input', side_effect=['10', '1'])
    def test_get_player_count_control_max(self, input_patched):
        scrabble_cli = ScrabbleCli(player_count=1)
        self.assertEqual(scrabble_cli.get_player_count(),1)

    @patch('builtins.input', side_effect=['Y']) 
    def test_skip_turn(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=1)
        result = scrabble_cli.skip_turn()
        self.assertEqual(result, None)  

    @patch('builtins.input', side_effect=['N']) 
    def test_do_not_skip_turn(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=1)
        result = scrabble_cli.skip_turn()
        self.assertEqual(result, "Please enter a word.")

    def test_draw_tiles_first_time(self):
        game = ScrabbleGame(players_count=2) 
        cli = ScrabbleCli(player_count=2)
        cli.game = game  
        player = game.players[0]
        player.tiles.extend([])  
        cli.draw_tiles()
        self.assertEqual(len(player.tiles), 7)

    def test_draw_tiles(self):
        game = ScrabbleGame(players_count=2)  
        cli = ScrabbleCli(player_count=2)
        cli.game = game  
        player = game.players[0]
        player.tiles.extend(["A", "B", "C"]) 
        cli.draw_tiles()
        self.assertEqual(len(player.tiles), 7)

    def test_show_tiles(self):
        scrabble_cli = ScrabbleCli(player_count=0)
        player = Player()  
        example_tiles = [('A', 1), ('B', 3), ('C', 3), ('D', 2)]
        player.tiles = example_tiles
        scrabble_cli.game.current_player = 0 
        scrabble_cli.game.players.append(player)
        with unittest.mock.patch('sys.stdout', new_callable= StringIO) as mock_stdout:
            scrabble_cli.show_tiles(player)
            printed_output = mock_stdout.getvalue()
        expected_output = "'s tiles: [('A', 1), ('B', 3), ('C', 3), ('D', 2)]\n"
        self.assertEqual(printed_output, expected_output)

    @patch('builtins.print') 
    def test_show_board(self, mock_print):
        scrabble_cli = ScrabbleCli(player_count=2)
        scrabble_cli.show_board()
        mock_print.assert_called_once_with(scrabble_cli.game.board.show_board())

    @patch('builtins.input', side_effect=[ "TAZA", '7', '7', 'H'])
    def test_get_word_location_orientation(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=2)
        word, location, orientation = scrabble_cli.get_word_location_orientation()
        self.assertEqual(word, 'TAZA')
        self.assertEqual(location, (7,7))
        self.assertEqual(orientation, 'H')

    @patch('builtins.input', side_effect=[ '0'])
    def test_get_word_location_orientation_return(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=2)
        word, location, orientation = scrabble_cli.get_word_location_orientation()
        self.assertEqual(word, '0')
        self.assertEqual(location, None)
        self.assertEqual(orientation, None)

    @patch('builtins.input', side_effect=['2'])
    @patch.object(ScrabbleCli, 'get_word_location_orientation', return_value=('HOLA', (7, 7), 'H'))
    def test_placed_word(self, mock_get_word, mock_input):
        scrabble_cli = ScrabbleCli(player_count=2)
        game = ScrabbleGame(players_count=2)
        scrabble_cli.game.next_turn()
        player = game.players[game.current_player]
        game.players[game.current_player].tiles = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        scrabble_cli.place_and_put_word()
        game.put_on_the_board_first_time('HOLA', [7,7], 'H')
        self.assertEqual(len(game.players[game.current_player].tiles), 0)
        # self.assertEqual(player.get_score(), 7)
        self.assertEqual(game.board.grid[7][7].tile, 'H')
        self.assertEqual(game.board.grid[7][8].tile, 'O')
        self.assertEqual(game.board.grid[7][9].tile, 'L')
        self.assertEqual(game.board.grid[7][10].tile, 'A')

    @patch('builtins.input', side_effect=['2', '1 2 3 4', '0'])
    def test_exchange_tiles(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=2)
        player = scrabble_cli.game.players[0]
        player.tiles = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        scrabble_cli.exchange()
        self.assertEqual(len(player.tiles), 4)

    @patch.object(ScrabbleCli, "print_welcome_message")
    @patch.object(ScrabbleCli, "get_player_count")
    @patch.object(ScrabbleCli, "get_player_names")
    @patch.object(ScrabbleCli, "draw_tiles")
    @patch.object(ScrabbleCli, "show_tiles")
    @patch.object(ScrabbleCli, "show_board")
    @patch.object(ScrabbleCli, "player_turn")
    @patch.object(ScrabbleGame, "is_game_over")
    def test_start_game(self, mock_print_welcome_message, mock_get_player_count, mock_get_player_names, mock_draw_tiles, mock_show_tiles, mock_show_board, mock_player_turn, mock_is_game_over):
        mock_is_game_over.return_value = True
        scrabble_cli = ScrabbleCli(player_count=2)
        scrabble_cli.start_game()

    @patch.object(ScrabbleGame, "comprobate_is_a_number")
    @patch.object(ScrabbleCli, "player_playing")
    def test_player_turn_play(self, mock_player_playing, mock_comprobate_is_a_number):
        scrabble_cli = ScrabbleCli(player_count=2)
        with patch('builtins.input', return_value = 1) as mock_input:
            scrabble_cli.player_turn()
        self.assertEqual(mock_input.call_count, 1)

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

    # def test_game_can_be_played_with_2_players(self):
    #     game = ScrabbleGame(2)
    #     self.assertEqual(len(game.players), 2)

    # def test_game_can_be_played_with_3_players(self):
    #     game = ScrabbleGame(3)
    #     self.assertEqual(len(game.players), 3)

    # def test_game_can_be_played_with_4_players(self):
    #     game = ScrabbleGame(4)
    #     self.assertEqual(len(game.players), 4)

if __name__ == "__main__":
    unittest.main()
