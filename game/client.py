from game.scrabble import ScrabbleGame
from game.board import Board,NoCenterLetterException
from game.player import Player

def get_player_names(player_count):
    player_names = []
    for i in range(player_count):
        name = input(f"Enter the name for player {i + 1}: ")
        player = Player() 
        player.write_name(name)
        player_names.append(name)
    return player_names

def get_player_count():
    while True:
        try:
            player_count = int(input('cantidad de jugadores (1-3): '))
            if player_count <= 3:
                break
        except Exception as e:
            print('ingrese un numero por favor: ')
    return player_count

def main():
    print("Que comience el juego!")
    names = get_player_names(player_count=0)
    scrabble_game = ScrabbleGame(players_count=get_player_count())
    print("Ingrese la cantidad de jugadores: ", len(scrabble_game.players))
    # scrabble_game.next_turn()
    print(f"Turno del jugador {scrabble_game.current_player.id}")
    game = ScrabbleGame(get_player_count())
    print('La cantidad de jugadores es: ' + str(get_player_count()))
    game.next_turn()
    print(f"Turno del jugador 1")
    word = input('Ingrese palabra: ')
    location_x = input('Ingrese posición X: ')
    location_y = input('Ingrese posición Y: ')
    board = Board()
    try:
        board.put_word_first_time(word, location, orientation)
    except NoCenterLetterException as e:
        print(e.message)

    location = (location_x, location_y)
    orientation = input('Ingrese orientación (V/H): ')
    scrabble_game.validate_word(word)
    return names

if __name__ == '__main__':
    main()