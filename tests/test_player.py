import unittest
from game.player import Player,NotEnoughTilesException
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def test__init__(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles),0)
    
    def test_set_name(self):
        player = Player()
        player.write_name('Victoria')
        self.assertEqual(player.get_name(), 'Victoria')

    def test_take_tiles(self):
        player=Player()
        bag = BagTiles()
        player.take_tiles(bag, 7)
        self.assertEqual(len(player.tiles), 7)

    def test_validateuserhasletters(self):
        bag_tile = BagTiles()
        player = Player()
        bag_tile.tiles = [
            Tile(letter='H', value=4, cant=2),
            Tile(letter='O', value=1, cant=9),
            Tile(letter='L', value=1, cant=4),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
            Tile(letter='A', value=1, cant=12),
        ]
        tiles = [
            Tile(letter='H', value=4, cant=2),
            Tile(letter='O', value=1, cant=9),
            Tile(letter='L', value=1, cant=4),
            Tile(letter='A', value=1, cant=12),
        ]
        player.tiles = bag_tile.tiles 
        is_valid = player.has_letters(tiles)
        self.assertEqual(is_valid, True)

    def test_validatefailwhenuserhasnotletters(self):
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

    def test_exchange_tiles(self):
        player = Player()
        bag = BagTiles()
        player.tiles = [Tile('A', 1, 12), Tile('B', 3, 2), Tile('C', 2, 4)]
        exchanged_tiles, new_tiles = player.exchange_tiles(bag, tiles_to_exchange=[0])
        self.assertNotEqual(exchanged_tiles[0], player.tiles[0])

    def test_remove_letters_from_hand(self):
        player = Player()
        player.tiles = ["A", "L", "C", "D", "A"]
        player.remove_letters_from_hand("ALA")
        self.assertEqual(player.tiles, ["C", "D"])

    def test_show_tiles(self):
        player = Player()
        self.assertEqual(player.show_tiles(), player.tiles)

    def test_score(self):
        player = Player()
        player.increase_score(3)
        self.assertEqual(player.get_score(), 3)

if __name__ == '__main__':
    unittest.main()

