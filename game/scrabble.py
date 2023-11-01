from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import validate_word
from game.cell import Cell
from game.scrabble2 import Scrabble2

class NoValidWordException(Exception):
    pass

class NoEnoughTilesException(Exception):
    pass

class NoNeededLettersException(Exception):
    pass


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.cell = Cell(multiplier=1, multiplier_type='')
        self.scrabble2 = Scrabble2()
        self.players = []
        self.turn = 0
        self.current_player = 0
        self.game_state = None
        self.round_number = 0
        for _ in range(players_count):
            self.players.append(Player())
        
    def start_game(self):
        self.game_state = 'started'

    def put_on_the_board_first(self, word, location, orientation):
        if not validate_word(word):
            raise NoValidWordException('Invalid word')
        self.board.put_word_first_time(word, location, orientation)
        self.next_turn()

    def correct_word(self, word, location, orientation):
        if not validate_word(word):
            raise NoValidWordException('Invalid word')
        self.board.is_word_connected(word,location,orientation)
        self.board.validate_word_place_board(word, location, orientation)
        return True
    
    def put_word_not_first(self,word,location,orientacion):
        if self.correct_word(word,location,orientacion):
            self.board.put_words(word,location,orientacion)
        self.next_turn()
        return True
    
    def check_first_turn(self):
        return self.board.is_empty()

    def give_initial_player_tiles(self, player_index):
        player = self.players[player_index]
        player.get_tiles(self.bag_tiles, 7)
        self.next_turn()

    def give_initial_tiles_to_all_players(self):
        for player_index in range(len(self.players)):
            self.give_initial_player_tiles(player_index)

    def give_player_tiles(self, player_index, amount):
        player = self.players[player_index]
        if len(player.tiles) + amount > 7:
            amount = 7 - len(player.tiles)  
        player.get_tiles(self.bag_tiles, amount)
        self.next_turn()

    def get_scores(self):
        scores = {}
        for player in self.players:
            scores[player.get_name()] = player.get_score()
        return scores

    def is_game_over(self):
        self.game_state = 'over'
        if len(self.bag_tiles) == 0:
            return True
        return False

    def check_is_number(self, string):
        try:
            return int(string)
        except ValueError:
            return None
        
    def check_is_orientation(self, orientation):
        real_orientation = ['H', 'V']
        if orientation in real_orientation:
            return orientation
        else:
            return None
        
    def get_score(self, player_index):
        return self.players[player_index].get_score()
    
    def calculate_score_words(self, new_words, start, orientation):
        total_score = 0
        player = self.players[self.current_player]
        for word_info in new_words:
            word, start, orientation = word_info
            word_cells = self.board.word_to_cells(word, start[0], start[1], orientation)
            word_value = self.scrabble2.calculate_word_value(word_cells, start, orientation)
            total_score += word_value
        # Detectar palabras secundarias
            secondary_words = self.board.detect_secondary_words(word, start, orientation)
            for secondary_word_info in secondary_words:
                secondary_word, secondary_start, secondary_orientation = secondary_word_info
                secondary_word_cells = self.board.word_to_cells(secondary_word, secondary_start[0], secondary_start[1], secondary_orientation)
                secondary_word_value = self.scrabble2.calculate_word_value(secondary_word_cells, secondary_start, secondary_orientation)
                total_score += secondary_word_value
        player.increase_score(total_score)

    def play_word(self, word, location, orientation):
        current_player = self.players[self.current_player]
        if current_player.has_letters(word):
                current_player.remove_letters_from_hand(word)
        else:
            raise NoNeededLettersException('No tienes las letras necesarias para esta palabra')

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
    
        
    def is_game_over(self):
        if len(self.bag_tiles) == 0:
            return True
        return False
    
