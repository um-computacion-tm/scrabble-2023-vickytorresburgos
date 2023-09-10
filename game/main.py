from game.scrabble import ScrabbleGame

def main():
    player_count = int(input('cantidad de jugadores'))
    game = ScrabbleGame(player_count)
    while(game.playing()):