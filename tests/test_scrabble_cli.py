import unittest
from game.scrabble_cli import *
from unittest.mock import patch
from io import StringIO

class TestCli(unittest.TestCase): 
    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        self.assertEqual(
            players_to_play(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', "10", '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        self.assertEqual(
            players_to_play(),
            3,
        )
        
    @patch('builtins.input', return_value="3")
    def test_init(self, mock_input):
        cli = ScrabbleCli(mock_input)
        self.assertIsInstance(cli.game, ScrabbleGame)
    
       
    @patch('builtins.input', side_effect=['Alice', 'Bob', 'Charlie'])
    def test_scrabble_cli_with_names(self, mock_input):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.name_players(3)        
        expected_names = ['Alice', 'Bob', 'Charlie']
        for i in range(3):
            self.assertEqual(scrabble_cli.game.players[i].name, expected_names[i])
            
    @patch('builtins.print')
    def test_show_score(self, print_patched):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.score = 40
        scrabble_cli.show_score()
        
    @patch('builtins.print')
    def test_show_player_tiles(self, print_patched):
        scrabble_cli = ScrabbleCli(3)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            Tile("A",1),
            Tile("B",2)
        ]
        scrabble_cli.show_tiles()
        
    @patch('builtins.print')
    def test_show_current_player(self, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.name = "Juan"
        scrabble_cli.show_current_player()
        
    @patch('builtins.input', return_value='2')
    def test_exchange_tiles(self, input_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            Tile("A",1),
            Tile("B",2),
            Tile("C",3),
            Tile("D",4),
            Tile("E",5),
            Tile("F",6),
            Tile("G",7)
        ]
        scrabble_cli.exchange_index_tile()
        
    @patch('builtins.input', return_value="H")
    def test_choose_wildcard(self, input_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            Tile(" ",0),
        ]
        scrabble_cli.choose_wildcard()
        self.assertEqual(scrabble_cli.game.current_player.tiles[0].letter, "H")
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', "16", '3'])
    def test_get_row(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_row()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['F', "-3", '7'])
    def test_get_col(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_col()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['F', "3", 'H'])
    def test_get_orientation_horizontal(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_orientation()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', "Vertical", 'V'])
    def test_get_orientation_vertical(self, input_patched, print_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.get_orientation()
        
    def test_end_current_turn(self):
        scrabble_cli = ScrabbleCli(2)

        with self.assertRaises(EndTurnException):
            scrabble_cli.end_current_turn()
        
    @patch('builtins.input', return_value="Y")
    def test_vote_to_end_game(self, input_patched):
        scrabble_cli = ScrabbleCli(1)
        scrabble_cli.vote_to_end_game()
        self.assertEqual(scrabble_cli.game.votes, ["Y"])
       
      
    @patch('builtins.input', side_effect=["perro", "7", "7", "H", "go back"])
    @patch('builtins.print')
    def test_enter_word_valid_input_and_go_back(self, mock_input, mock_print):
        
        scrabble_cli = ScrabbleCli(2)  
        
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            Tile("A",1),
            Tile("H",1),
            Tile("O",1),
            Tile("L",1),
        ]
        
        scrabble_cli.enter_word()  
           
  
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["2","1","2"])
    def test_turn_exchange_tiles(self, mock_input, mock_print):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game.current_player.tiles = [
            Tile("A",1),
            Tile("H",1),
            Tile("O",1),
            Tile("L",1),
        ]
        scrabble_cli.game_turn()
        
    @patch('builtins.print')
    @patch('builtins.input', side_effect=["9","Y"])
    def test_turn_cote_to_end(self, mock_input, mock_print):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.current_player = scrabble_cli.game.players[0]
        scrabble_cli.game_turn()
               
               
    
    def test_show_results(self):
        
        scrabble_cli = ScrabbleCli(2)
        scrabble_cli.game.players[0].name = "E"
        scrabble_cli.game.players[0].score = 100
        scrabble_cli.game.players[1].name = "Tomas"
        scrabble_cli.game.players[1].score = 200
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            scrabble_cli.show_results()
            expected_output = "The Game has ended\n[('Tomas', 200), ('E', 100)]\nThe winner is: Tomas\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    
            
    
if __name__ == '__main__':
    unittest.main()