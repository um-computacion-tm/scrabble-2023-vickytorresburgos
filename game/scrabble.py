from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import validate_word
from game.cell import Cell

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.turn = 0
        self.current_player = None
        for _ in range(players_count):
            self.players.append(Player())
        
    def play(self, word, location, orientation):
        self.correct_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.calculate_word_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:  # Access to the last value of the list
            index = self.players.index(self.current_player)
            index = (index + 1) % len(self.players)  # Advance to the first player if it's the last
            self.current_player = self.players[index]
        else:
            index = self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
    
    def correct_word(self, word, location, orientation):
        validate_word(word)
        self.is_word_connected( word, location, orientation)
        self. validate_len_word_inside_board(word,location,orientation)
        self.validate_word_place_board(word, location, orientation)
        
    def is_game_over(self):
        if len(self.bag_tiles) == 0:
            return True
        return False