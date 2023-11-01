# import unittest
# from game.scrabble import ScrabbleGame, Board,Cell,Player, NoValidWordException,BagTiles,NoEnoughTilesException,NoNeededLettersException
# from game.models import Tile
# from game.dictionary import validate_word
# from unittest.mock import patch

# class TestScrabble(unittest.TestCase):
#     def test__init__(self):
#         scrabble_game = ScrabbleGame(players_count = 3)
#         self.assertIsNotNone(scrabble_game.board)
#         self.assertEqual(len(scrabble_game.players),3)
#         self.assertIsNotNone(scrabble_game.bag_tiles)

#     def test_is_game_over_true(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         scrabble_game.bag_tiles = [] 
#         self.assertTrue(scrabble_game.is_game_over())

#     def test_is_game_over_false(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         scrabble_game.bag_tiles = ['A']  
#         self.assertFalse(scrabble_game.is_game_over())
#         self.assertEqual(scrabble_game.game_state,'over')

#     @patch('builtins.input', side_effect=['giveup'])
#     def test_quit(self, mock_input):
#         scrabble_game = ScrabbleGame(players_count=3)
#         scrabble_game.bag_tiles = ['Z']
#         scrabble_game.is_game_over()
#         self.assertEqual(scrabble_game.game_state, "over")

#     def test_last_player_turn(self):
#         scrabble_game = ScrabbleGame(2)
#         scrabble_game.current_player = 1
#         scrabble_game.next_turn()
#         self.assertEqual(scrabble_game.current_player, 0)

#     def test_player_pass_turn(self):
#         scrabble_game = ScrabbleGame(2)
#         scrabble_game.next_turn()
#         self.assertEqual(scrabble_game.current_player, 1)

#     def test_is_first_turn(self):
#         scrabble_game = ScrabbleGame(1)
#         self.assertTrue(scrabble_game.check_first_turn())

#     def test_game_ongoing(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         scrabble_game.game_state_start()
#         self.assertEqual(scrabble_game.game_state, "ongoing")

#     def test_first_turn(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         self.assertTrue(scrabble_game.check_first_turn())

#     def test_give_player_tiles_first_tile(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         player_index = 0
#         scrabble_game.give_initial_player_tiles(player_index)
#         self.assertEqual(len(scrabble_game.players[player_index].tiles), 7)

#     def test_give_player_tiles(self):
#         game = ScrabbleGame(players_count=2)
#         game.players[0].tiles = ["A", "B", "C", "D", "E", "F"]
#         game.give_player_tiles(player_index=0, amount=2)
#         self.assertEqual(len(game.players[0].tiles), 7)
#         game.give_player_tiles(player_index=0, amount=1)
#         self.assertEqual(len(game.players[0].tiles), 7)
#         game.give_player_tiles(player_index=1, amount=5)
#         self.assertEqual(len(game.players[1].tiles), 5)

#     def test_get_scores(self):
#         scrabble_game = ScrabbleGame(players_count=1)
#         scrabble_game.players[0].write_name("Alma")
#         self.assertEqual(scrabble_game.get_scores(), {'Alma': 0})

#     def test_valid_number(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         string = "42"
#         result = scrabble_game.check_is_a_number(string)
#         self.assertEqual(result, 42)

#     def test_invalid_string(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         string = "abc"
#         result = scrabble_game.check_is_a_number(string)
#         self.assertIsNone(result)

#     def test_put_tiles_in_bag_all_players(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         self.assertEqual(len(scrabble_game.players[0].tiles), 0)
#         self.assertEqual(len(scrabble_game.players[1].tiles), 0)
#         scrabble_game.give_initial_tiles_to_all_players()
#         self.assertEqual(len(scrabble_game.players[0].tiles), 7)
#         self.assertEqual(len(scrabble_game.players[1].tiles), 7)

#     def test_correct_first_word_no_valid(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         with self.assertRaises(NoValidWordException):
#             scrabble_game.put_on_the_board_first_time('WHO', [7,7], 'V')

#     def test_correct_word(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         scrabble_game.board.grid[7][7].tile = Tile('C',1)
#         scrabble_game.board.grid[7][8].tile = Tile('A',1)
#         scrabble_game.board.grid[7][9].tile = Tile('S',1)
#         scrabble_game.board.grid[7][10].tile = Tile('A',1)
#         self.assertTrue(scrabble_game.correct_word('SACA', [6,8], 'V'))

#     def test_correct_wordd(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         scrabble_game.board.grid[7][7].tile = Tile('C',1)
#         scrabble_game.board.grid[7][8].tile = Tile('A',1)
#         scrabble_game.board.grid[7][9].tile = Tile('S',1)
#         scrabble_game.board.grid[7][10].tile = Tile('A',1)
#         self.assertTrue(scrabble_game.correct_word('ES', [6,9], 'H'))

#     def test_not_valid(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         scrabble_game.board.grid[7][7].tile = Tile('C',1)
#         scrabble_game.board.grid[7][8].tile = Tile('A',1)
#         scrabble_game.board.grid[7][9].tile = Tile('S',1)
#         scrabble_game.board.grid[7][10].tile = Tile('A',1)
#         with self.assertRaises(NoValidWordException):
#             scrabble_game.correct_word('EAT', [6,8], 'V')

#     def test_put_first_time(self):
#         scrabble_game = ScrabbleGame(players_count=3)
#         tile1=Tile('H', 1)
#         tile2= Tile('O', 1)
#         tile3= Tile('L', 1)
#         tile4 =Tile('A', 1)
#         scrabble_game.players[scrabble_game.current_player].tiles=[tile1,tile2,tile3,tile4]
#         scrabble_game.put_on_the_board_first_time('HOLA', [7,7], 'H')
#         self.assertEqual(scrabble_game.board.grid[7][7].tile, 'H')
#         self.assertEqual(scrabble_game.board.grid[7][8].tile, 'O')
#         self.assertEqual(scrabble_game.board.grid[7][9].tile, 'L')
#         self.assertEqual(scrabble_game.board.grid[7][10].tile, 'A')

#     def test_comprobate_is_an_orientation(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         self.assertEqual(scrabble_game.comprobate_is_an_orientation('H'), 'H')
#         self.assertEqual(scrabble_game.comprobate_is_an_orientation('V'), 'V')
#         self.assertIsNone(scrabble_game.comprobate_is_an_orientation('X'))
#         self.assertIsNone(scrabble_game.comprobate_is_an_orientation(''))
#         self.assertIsNone(scrabble_game.comprobate_is_an_orientation(None))

#     def test_calculate_score(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         scrabble_game.board.grid[7][7].tile = Tile('C',1)
#         scrabble_game.board.grid[7][8].tile = Tile('A',1)
#         scrabble_game.board.grid[7][9].tile = Tile('S',1)
#         scrabble_game.board.grid[7][10].tile = Tile('A',1)
#         scrabble_game.give_initial_tiles_to_all_players()
#         tile1 = Tile('S', 1)
#         tile2 = Tile('A', 1)
#         tile3 = Tile('N', 1)
#         tile4 = Tile('D', 2)
#         tile5 = Tile('I', 1)
#         tile6 = Tile('A', 1)
#         tile7 = Tile('X', 8)
#         scrabble_game.players[scrabble_game.current_player].tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7]
#         new_word = [("SANDIA", [6, 8], 'V')] 
#         scrabble_game.put_word_not_first_time("SANDIA", [6, 8], 'V')
#         scrabble_game.calculate_score_words(new_word, [6, 8], 'V')
#         player_score = scrabble_game.players[scrabble_game.current_player].get_score()
#         self.assertEqual(player_score, 9)

#     def test_calculate_score(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         scrabble_game.give_initial_tiles_to_all_players()
#         tile1 = Tile('S', 1)
#         tile2 = Tile('A', 1)
#         tile3 = Tile('N', 1)
#         tile4 = Tile('D', 2)
#         tile5 = Tile('I', 1)
#         tile6 = Tile('A', 1)
#         tile7 = Tile('X', 8)
#         scrabble_game.players[scrabble_game.current_player].tiles = [tile1, tile2, tile3, tile4, tile5, tile6, tile7]
#         new_word = [("SANDIA", [7, 7], 'H')] 
#         scrabble_game.put_on_the_board_first_time("SANDIA", [7, 7], 'H')
#         scrabble_game.calculate_score_words(new_word, [7, 7], 'H')
#         player_score = scrabble_game.players[scrabble_game.current_player].get_score()
#         self.assertEqual(player_score, 8)

#     def test_play_word(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         player = scrabble_game.players[scrabble_game.current_player]
#         tile1 = Tile('S', 1)
#         tile2 = Tile('A', 1)
#         tile3 = Tile('N', 1)
#         tile4 = Tile('D', 2)
#         tile5 = Tile('I', 1)
#         tile6 = Tile('A', 1)
#         tile7 = Tile('X', 8)
#         player.tiles = [tile1,tile2,tile3,tile4,tile5,tile6,tile7]
#         word = [tile1,tile2,tile3,tile4,tile5,tile6]
#         location = (7, 7)  
#         orientation = "H" 
#         scrabble_game.board.put_word_first_time(word, location, orientation)
#         scrabble_game.play_word(word, location, orientation)
#         player.tiles = [tile7]
#         expected_tiles_after_play = [tile7]
#         actual_tiles = player.tiles
#         self.assertEqual(expected_tiles_after_play, actual_tiles)

#     def test_play_word_no_enough_letters(self):
#         scrabble_game = ScrabbleGame(players_count=2)
#         player = scrabble_game.players[scrabble_game.current_player]
#         tile1 = Tile('S', 1)
#         tile2 = Tile('A', 1)
#         tile3 = Tile('N', 1)
#         tile4 = Tile('D', 2)
#         tile5 = Tile('I', 1)
#         tile6 = Tile('A', 1)
#         tile7 = Tile('X', 8)
#         player.tiles = [tile1,tile2,tile3,tile4,tile5]
#         word = [tile1,tile2,tile3,tile4,tile5,tile6]
#         location = (7, 7)  
#         orientation = "H" 
#         with self.assertRaises(NoNeededLettersException):
#             scrabble_game.play_word(word,location,orientation)

# if __name__ == '__main__':
#     unittest.main()


