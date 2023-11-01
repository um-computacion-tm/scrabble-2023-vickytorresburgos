from io import StringIO
import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.tiles import Tile
from game.player import Player
from game.dictionary import Dictionary
from game.scrabble import end_game
class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]
    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[1]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[2]
    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
 
        assert scrabble_game.current_player == scrabble_game.players[0]
    def test_validate_diccionari_word(self):
       
       game=ScrabbleGame(3)
       self.assertTrue(game.validate_dictionary_word("auto"))

    def test_end_game(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = []
        scrabble_game.current_player = scrabble_game.players[0]
        with self.assertRaises(end_game) as context:
            scrabble_game.end_game()
            
    def test_end_game_fail(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = [
            Tile(letter='H', value=3),
            Tile(letter='O', value=1)
            ]
        game_finish = scrabble_game.end_game()
        self.assertFalse(game_finish, False) 
        
    def test_full_board(self):
        scrabble_game = ScrabbleGame(players_count=2)
        for row in  scrabble_game.board.grid:
            for cell in row:
                cell.letter = Tile("A",1)
        complete_board = scrabble_game.full_board()
        self.assertEqual(complete_board,True) 
        with self.assertRaises(end_game):
          scrabble_game.end_game()    
        

    def test_fill_player_tiles(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile(letter="H", value=3)  
            ]
        scrabble_game.fill_current_player_tiles()
        self.assertEqual(scrabble_game.current_player.tiles[0].letter, "H")
        self.assertEqual(scrabble_game.current_player.tiles[0].value, 3)  
    
    def test_put_word_horizontal(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile(letter='H', value=3),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        word = "Hola"
        orientation = "H"
        location = (7,7)
        scrabble_game.put_words(word,location,orientation)
        self.assertEqual(scrabble_game.board.grid[7][7].letter.letter, "H") 
        self.assertEqual(scrabble_game.board.grid[7][8].letter.letter, "O") 
        self.assertEqual(scrabble_game.board.grid[7][9].letter.letter, "L") 
        self.assertEqual(scrabble_game.board.grid[7][10].letter.letter, "A")  
        self.assertEqual(scrabble_game.current_player.tiles,[])
    
    def test_put_word_vertical(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.bag_tiles.tiles = [
            Tile(letter='H', value=3),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='H', value=3),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(5))
        word = "Hola"
        orientation = "V"
        location = (7,7)
        scrabble_game.put_words(word,location,orientation)
        self.assertEqual(scrabble_game.board.grid[7][7].letter.letter, "H") 
        self.assertEqual(scrabble_game.board.grid[8][7].letter.letter, "O") 
        self.assertEqual(scrabble_game.board.grid[9][7].letter.letter, "L") 
        self.assertEqual(scrabble_game.board.grid[10][7].letter.letter, "A") 
        self.assertEqual(scrabble_game.current_player.tiles[0].letter,"H")
        self.assertEqual(scrabble_game.current_player.tiles[0].value,3)
    def test_check_word_to_str(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.board.grid[7][7].add_letter(Tile('C', 3))
        scrabble_game.board.grid[7][8].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][9].add_letter(Tile('S', 1)) 
        scrabble_game.board.grid[7][10].add_letter(Tile('A', 1)) 
        word = scrabble_game.board.check_word_left(row=7, col=11)
        word_from_list = scrabble_game.check_word_to_str(word)
        self.assertEqual(word_from_list, "CASA")
    def test_validate_check_word(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.board.grid[7][7].add_letter(Tile('C', 3))
        scrabble_game.board.grid[7][8].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][9].add_letter(Tile('S', 1)) 
        scrabble_game.board.grid[7][10].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][11].add_letter(Tile('D', 3)) 
        scrabble_game.board.grid[7][12].add_letter(Tile('O', 1)) 
        scrabble_game.board.grid[7][13].add_letter(Tile('S', 1)) 
        word = scrabble_game.board.check_word_horizontal(row=7, col=11)
        word_from_list = scrabble_game.check_word_to_str(word)
        validation = scrabble_game.validate_check_word(word_from_list)
        self.assertEqual(validation, True)
   
    def test_get_word_vertical(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.board.grid[7][7].add_letter(Tile('P', 1))
        scrabble_game.board.grid[7][8].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][9].add_letter(Tile('T', 1)) 
        scrabble_game.board.grid[7][10].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][7].state = False
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 1),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
            Tile('S', 1),
        ]
        word = "casas"
        location = (3,11)
        orientation = "V"
        scrabble_game.put_words(word, location, orientation)
        scrabble_game.add_score(word, location, orientation)
        scrabble_game.get_words(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score,10)
        
    def test_get_word_vertical_no_sum_word_on_board(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.board.grid[7][7].add_letter(Tile('P', 1))
        scrabble_game.board.grid[7][8].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][9].add_letter(Tile('T', 1)) 
        scrabble_game.board.grid[7][10].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][7].state = False
        scrabble_game.board.grid[7][8].state = False
        scrabble_game.board.grid[7][9].state = False
        scrabble_game.board.grid[7][10].state = False
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 1),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
        ]
        word = "casa"
        location = (6,8)
        orientation = "V"
        scrabble_game.put_words(word, location, orientation)
        scrabble_game.add_score(word, location, orientation)
        scrabble_game.get_words(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score,4)
        
    def test_get_word_horizontal(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.board.grid[7][7].add_letter(Tile('P', 1))
        scrabble_game.board.grid[8][7].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[9][7].add_letter(Tile('T', 1)) 
        scrabble_game.board.grid[10][7].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[7][7].state= False
        scrabble_game.board.grid[8][7].state= False
        scrabble_game.board.grid[9][7].state= False
        scrabble_game.board.grid[10][7].state = False
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 1),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
            Tile('S', 1),
        ]
        word = "casas"
        location = (11,3)
        orientation = "H"
        scrabble_game.put_words(word, location, orientation)
        scrabble_game.add_score(word, location, orientation)
        scrabble_game.get_words(word, location, orientation)
        self.assertEqual(scrabble_game.current_player.score,17)
        
    def test_get_word_horizontal(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.board.grid[7][7].add_letter(Tile('P', 1))
        scrabble_game.board.grid[8][7].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[9][7].add_letter(Tile('T', 1)) 
        scrabble_game.board.grid[10][7].add_letter(Tile('A', 1)) 
        scrabble_game.board.grid[12][7].add_letter(Tile('I', 1))
        scrabble_game.board.grid[13][7].add_letter(Tile('T', 1))  
        scrabble_game.board.grid[7][7].state= False
        scrabble_game.board.grid[8][7].state= False
        scrabble_game.board.grid[9][7].state= False
        scrabble_game.board.grid[10][7].state = False
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.current_player.tiles = [
            Tile('C', 1),
            Tile('A', 1),
            Tile('S', 1),
            Tile('A', 1),
            Tile('S', 1),
        ]
        word = "casas"
        location = (11,3)
        orientation = "H"
        scrabble_game.put_words(word, location, orientation)
        scrabble_game.add_score(word, location, orientation)
        scrabble_game.get_words(word, location, orientation)
        self.assertEqual(scrabble_game.get_words(word, location, orientation),False)
    def test_score_board(self):
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = "Rogelio"
        scrabble_game.players[0].score = 40
        scrabble_game.players[1].name = "Apu"
        scrabble_game.players[1].score = 14
        scoreboard = scrabble_game.sort_players_by_score()
        self.assertEqual(scoreboard[0][0],"Rogelio")
        self.assertEqual(scoreboard[0][1],40)
        self.assertEqual(scoreboard[1][0],"Apu")
        self.assertEqual(scoreboard[1][1],14)
    def test_return_old_situation(self):
        scrabble_game = ScrabbleGame(1)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.player_old_score = 0
        scrabble_game.bag_tiles.tiles = [
            Tile(letter='P', value=3),
            Tile(letter='A', value=1),
            Tile(letter='T', value=1),
            Tile(letter='A', value=1),
        ]
        scrabble_game.current_player.tiles.extend(scrabble_game.bag_tiles.take(4))
        scrabble_game.put_words(word = "Pata",location = (7,7), orientation = "V")
        scrabble_game.add_score(word = "Pata",location = (7,7), orientation = "V")
        scrabble_game.return_old_situation(word = "Pata",location = (7,7), orientation = "V")
        self.assertEqual(len(scrabble_game.current_player.tiles), 4)
        self.assertEqual(scrabble_game.current_player.score, 0)
        self.assertEqual(scrabble_game.board.grid[7][7].letter, None)
        self.assertEqual(scrabble_game.board.grid[8][7].letter, None)
        self.assertEqual(scrabble_game.board.grid[9][7].letter, None)
        self.assertEqual(scrabble_game.board.grid[10][7].letter, None)
        self.assertEqual(scrabble_game.board.grid[7][7].state, True)
        self.assertEqual(scrabble_game.board.grid[8][7].state, True)
        self.assertEqual(scrabble_game.board.grid[9][7].state, True)
        self.assertEqual(scrabble_game.board.grid[10][7].state, True)
if __name__ == '__main__':
    unittest.main()