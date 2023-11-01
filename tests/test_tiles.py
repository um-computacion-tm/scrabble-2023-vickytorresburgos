
import unittest
from game.tiles import Tile
from game.bagtiles import BagTiles
from unittest.mock import patch
class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A',1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
    def test_get_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, tile.get_letter()) 
    def test_get_value(self):
        tile=Tile('B',3)
        self.assertEqual(tile.value,tile.get_value())   
class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )
    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )
    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 10), Tile('Y', 4)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            102,
        )
    def test_set_letter(self):
        tile = Tile('A', 1)
        tile.set_letter("B")
        self.assertEqual(tile.letter, "B")
    def test_shuffle(self):
        bag_1 = BagTiles()
        bag_1.tiles =  [Tile('Z', 1), Tile('Y', 1), Tile('D', 1), Tile('C', 1), Tile('B', 1), Tile('A', 1)]
        bag_2 = BagTiles()
        bag_2.tiles = bag_1.tiles.copy()
        bag_2.shuffle_bag()
        self.assertNotEqual(bag_1.tiles, bag_2.tiles)
        self.assertCountEqual(bag_1.tiles, bag_2.tiles)   
    def test_repr_with_tile(self):
        tile = Tile("A",1)
        expected = "(A, 1)"  
        self.assertEqual(repr(tile), expected) 
if __name__ == '__main__':
    unittest.main()