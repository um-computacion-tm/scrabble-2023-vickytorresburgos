import unittest
from game.scrabble import ScrabbleGame, Board

class TestScrabble(unittest.TestCase):
    def test__init__(self):
        scrabble_game = ScrabbleGame(players_count = 3)
        self.assertIsNotNone(scrabble_game.board)

        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_is_game_over_true(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles = []  # Empty the bag tiles
        #Verify that the game is over
        self.assertTrue(scrabble_game.is_game_over())

    def test_is_game_over_false(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles = ['A']  # Empty the bag tiles
        #Verify that the game is over
        self.assertFalse(scrabble_game.is_game_over())

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]
        
    def test_next_turn_when_game_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_validate(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(scrabble_game.validate('facultad'), True)
        self.assertEqual(scrabble_game.validate('why'), False)

if __name__ == '__main__':
    unittest.main()