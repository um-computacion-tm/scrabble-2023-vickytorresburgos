from game.scrabble import ScrabbleGame, NoValidWordException,NoEnoughTilesException
from game.board import Board,NoCenterLetterException
from game.player import Player
from colorama import Fore, Style, init

class ScrabbleCli:
    def __init__(self,player_count):
        self.game = ScrabbleGame(players_count=player_count)
        self.first_time = True

    def start_game(self):
        self.print_welcome_message()
        player_count = self.get_player_count()
        player_names = self.get_player_names(player_count)
        self.draw_tiles()
    
        while not self.game.is_game_over():
            current_player = self.game.current_player
            player_name = player_names[current_player]
        
            print(f"It's {Fore.MAGENTA + player_name.upper() + Fore.RESET}'s turn:")
        
            self.show_tiles(player=Player)
            self.show_board()
            self.player_turn()

    def get_player_count(self):
        while True:
            try:
                player_count = int(input('Quantity of players (1-3): '))
                if 1 <= player_count <= 3:
                    return player_count
                else:
                    print('Please enter a number between 1 and 3.')
            except ValueError:
                print('Please enter a number.')

    def get_player_names(self, player_count):
        self.game.player_names = []
        for i in range(player_count):
            name = input(f"Enter the name for player {i + 1}: ")
            player = Player()
            player.write_name(name)
            self.game.players.append(player)
            self.game.player_names.append(name)
        return self.game.player_names

    def draw_tiles(self):
        current_player = self.game.players[self.game.current_player]
        if len(current_player.tiles) == 0:
            self.game.give_initial_tiles_to_all_players()
        else:
            if len(current_player.tiles) < 7:
                needed_tiles = 7 - len(current_player.tiles)
                self.game.give_player_tiles(self.game.current_player, needed_tiles)

    def player_turn(self):
        while True:
            action = input('What do you want to do? 1) Play / 2) Skip Turn / 3) Scores ')
            action = self.game.comprobate_is_a_number(action)
            if action == 1:
                self.player_playing()
                break
            elif action == 2:
                self.skip_turn()
            elif action == 3:
                self.show_scores()
        
    def player_playing(self):
        actions = {1: self.place_and_put_word, 2: self.exchange, 3: self.convert_joker, 4: self.quite_game }
        while True:
            action = input('What do you want to do? 1) Put / 2) Exchange / 3) Convert joker / 4) Skip ')
            action = self.game.comprobate_is_a_number(action)
            action_function = actions.get(action)
            if action_function is None:
                print('Invalid, try again')
            else:
                if action_function():
                    return True
            
    def convert_joker(self):
        current_player = self.game.players[self.game.current_player]
        tiles = current_player.tiles
        if '#' in [tile.letter for tile in tiles]:
            while True:
                letter_choice = input("Choose a letter for the wildcard (#): ")
                if len(letter_choice) == 1 and letter_choice.isalpha():
                    letter_choice = letter_choice.upper() 
                    for tile in tiles:
                        if tile.letter == '#':
                            tile.letter = letter_choice
                            break 
                    self.show_tiles(current_player)
                    break
                else:
                    print("Invalid letter. Please choose a single letter (A-Z).")
        else:
            print('You do not have a joker')
            
    def show_scores(self):
        print(Fore.YELLOW + "{:<15} {:<10}".format("Player", "Score") + Fore.RESET)
        print(Fore.YELLOW + "-" * 25 + Fore.RESET)
        for player in self.game.players:
            player_name = player.get_name().upper()
            player_score = player.get_score()
            print("{:<15} {:<10}".format(player_name, player_score))

    def place_and_put_word(self):
        while True:
            try:
                word, location, orientation = self.get_word_location_orientation()
                if word == '0':
                    break
                if self.first_time:
                    self.place_first_word(word, location, orientation)
                else:
                    self.place_word_not_first_time(word, location, orientation)
                return 'finish'
            except (NoValidWordException, NoEnoughTilesException) as e:
                print(f'Error: {e}')
                validate = input('You can return by pressing 0 or press any key to continue: ')
                if validate == '0':
                    break

    def place_first_word(self, word, location, orientation):
        try:
            success = self.game.put_on_the_board_first_time(word, location, orientation)
            if success:
                print("Palabra colocada exitosamente en el centro.")
                self.first_time = False
                self.game.calculate_score_words(new_words=None, start=0, orientation=None)
                self.game.play_word(word,location,orientation)
        except NoCenterLetterException as f:
            print(f'Error: {f}')
            validate = input('You can return by pressing 0 or press any key to continue: ')
            if validate == '0':
                return

    def place_word_not_first_time(self, word, location, orientation):
        if self.game.put_word_not_first_time(word, location, orientation):
            self.game.calculate_score_words(new_words=None, start=0, orientation=None)
            self.game.play_word(word,location,orientation)
            print("Palabra colocada exitosamente.")
    
    def get_word_location_orientation(self):
        while True:
            word = input('Put a word (0 to skip): ')
            if word == '0':
                return word, None, None
            location_x = input('Put the start row (0-14): ')
            location_x = self.game.comprobate_is_a_number(location_x)
            location_y = input('Put the start column (0-14): ')
            location_y = self.game.comprobate_is_a_number(location_y)
            location = (location_x, location_y)
            orientation = input('Put the orientation (V/H): ')
            orientation = orientation.strip().upper()
            orientation = self.game.comprobate_is_an_orientation(orientation)
            return word, location, orientation
        
    def exchange(self):
        player = self.game.players[self.game.current_player]
        while True:
            tiles_to_exchange = input("Choose the tiles you want to exchange; '0' to finish): ")
            if tiles_to_exchange == '0':
                break
            tiles_to_exchange = list(tiles_to_exchange)
            if all(tile.isnumeric() and 1 <= int(tile) <= 7 for tile in tiles_to_exchange):
                tiles_to_exchange = [int(tile) - 1 for tile in tiles_to_exchange]
                if all(0 <= index < len(player.tiles) for index in tiles_to_exchange):
                    exchanged_tiles, new_tiles = player.exchange_tiles(self.game.bag_tiles, tiles_to_exchange)
                    print(f"Exchanged tiles: {[tile for tile in exchanged_tiles]}")
                    print(f"New tile: {[tile for tile in new_tiles]}")
                    print(f'New tiles: {player.tiles}')
                    break
                else:
                    print("Invalid tile index. Please try again.")
            else:
                print("Invalid input. Please enter valid tile indices or '0' to finish).")
            
    def quite_game(self):
        return 'finish'

    def show_tiles(self,player):
        tiles = self.game.players[self.game.current_player].show_tiles()
        player_name = self.game.players[self.game.current_player].get_name()
        tiles_str = ", ".join([str(tile) for tile in tiles])
        print(f"{player_name}'s tiles: [{tiles_str}]")

    def print_welcome_message(self):
        init(autoreset=True)  
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Welcome to {Fore.RED}SCRABBLE {Style.RESET_ALL}")
        init() 

    def show_board(self):
        board_state = self.game.board.show_board()
        print(board_state)
    
    def skip_turn(self):
        response = input("Are you sure you would like to skip your turn? (Y/N): ")
        if response.upper() == "Y" or response.upper() == "y":
            self.game.next_turn()
        else:
            return "Please enter a word."

