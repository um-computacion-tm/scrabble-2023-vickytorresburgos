# import unittest
# from game.player import Player,NotEnoughTilesException
# from game.models import Tile, BagTiles

# class TestPlayer(unittest.TestCase):
#     def test__init__(self):
#         player_1 = Player()
#         self.assertEqual(len(player_1.tiles),0)
    
#     def test_set_name(self):
#         player = Player()
#         player.write_name('Alma')
#         self.assertEqual(player.get_name(), 'Alma')

#     def test_take_tiles(self):
#         player=Player()
#         bag = BagTiles()
#         player.take_tiles(bag, 7)
#         self.assertEqual(len(player.tiles), 7)

#     def test_validateuserhasletters(self):
#         bag_tile = BagTiles()
#         player = Player()
#         bag_tile.tiles = [
#             Tile(letter='H', value=1, cant=2),
#             Tile(letter='O', value=1, cant=9),
#             Tile(letter='L', value=1, cant=4),
#             Tile(letter='A', value=1, cant=12),
#             Tile(letter='A', value=1, cant=12),
#             Tile(letter='A', value=1, cant=12),
#             Tile(letter='A', value=1, cant=12),
#         ]
#         tiles = [
#             Tile(letter='H', value=1, cant=2),
#             Tile(letter='O', value=1, cant=9),
#             Tile(letter='L', value=1, cant=4),
#             Tile(letter='A', value=1, cant=12),
#         ]
#         player.tiles = bag_tile.tiles 
#         is_valid = player.has_letters(tiles)
#         self.assertEqual(is_valid, True)

#     def test_validatefailwhenuserhasnotletters(self):
#         bag_tile = BagTiles()
#         bag_tile.tiles = [
            # Tile(letter='H', value=1, cant=2),
            # Tile(letter='O', value=1, cant=9),
            # Tile(letter='L', value=1, cant=4),
            # Tile(letter='A', value=1, cant=12),
            # Tile(letter='A', value=1, cant=12),
            # Tile(letter='A', value=1, cant=12),
            # Tile(letter='A', value=1, cant=12),
#         ]
#         player = Player()
#         tiles = [
            # Tile(letter='H', value=1, cant=2),
            # Tile(letter='O', value=1, cant=9),
            # Tile(letter='L', value=1, cant=4),
            # Tile(letter='A', value=1, cant=12),
#         ]
#     def test_player_exchange(self):
#         player = Player()
#         bag = BagTiles()
#         player.take_tiles(bag, 2)
#         tile = player.tiles[0]
#         player.exchange_tiles(bag, 1)  
#         self.assertNotEqual(tile, player.tiles[0]) #verify that the exchanged tile is not the same as the original tile

#     def test_player_exchange_not_enough_tiles(self):
#         player = Player()
#         bag = BagTiles()
#         player.take_tiles(bag, 2)
#         with self.assertRaises(NotEnoughTilesException):
#             exchanged_tiles, new_tiles = player.exchange_tiles(bag, 3)
#         self.assertEqual(len(player.tiles), 2)  # Se espera que el jugador siga teniendo 2 fichas

#     def test_show_tiles(self):
#         player = Player()
#         self.assertEqual(player.show_tiles(), player.tiles)

#     def test_score(self):
#         player = Player()
#         player.increase_score(3)
#         self.assertEqual(player.get_score(), 3)

# if __name__ == '__main__':
#     unittest.main()

import unittest
from game.player import Player
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile(letter='H', value=1, cant=2),
            Tile(letter='O', value=1, cant=9),
            Tile(letter='L', value=1, cant=4),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
        ]
        tiles = [
            Tile(letter='H', value=1, cant=2),
            Tile(letter='O', value=1, cant=9),
            Tile(letter='L', value=1, cant=4),
            Tile(letter='A', value=1, cant=12),
        ]
        player.tiles = bag_tile.tiles
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=1, cant=2),
            Tile(letter='O', value=1, cant=9),
            Tile(letter='L', value=1, cant=4),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
        ]
        player = Player()
        tiles = [
            Tile(letter='H', value=1, cant=2),
            Tile(letter='O', value=1, cant=9),
            Tile(letter='L', value=1, cant=4),
            Tile(letter='A', value=1, cant=12),
        ]

        is_valid = player.has_letters(tiles)

        self.assertEqual(is_valid, False)

if __name__ == '__main__':
    unittest.main()
