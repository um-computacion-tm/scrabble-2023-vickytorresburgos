from game.scrabble_cli import*

def main():
    players = players_to_play()
    scrabble_game = ScrabbleCli(players)
    scrabble_game.name_players(len(scrabble_game.game.players))
 
    while True:
        try:
            scrabble_game.game.next_turn()
            scrabble_game.game.end_game()
            scrabble_game.show_current_player()  
            scrabble_game.game_turn()
            
        except end_game:
            scrabble_game.show_results()
            break

if __name__ == '__main__':
    main()