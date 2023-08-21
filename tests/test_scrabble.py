import unittest
from game.models import Tile, BagTiles
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tileA(self):
        tile = Tile('A', 1,12)
        self.assertEqual(tile.letter,'A')
        self.assertEqual(tile.value, 1)
        self.assertEqual(tile.cant, 12)

    def test_tileB(self):
        tile = Tile('B',3,2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 3)
        self.assertEqual(tile.cant, 2)
        
    def test_tileC(self):
        tile = Tile('C',3,4)
        self.assertEqual(tile.letter,'C')
        self.assertEqual(tile.value,3)
        self.assertEqual(tile.cant,4)


    def test_tileCH(self):
        tile = Tile('CH',5,1)
        self.assertEqual(tile.letter,'CH')
        self.assertEqual(tile.value,5)
        self.assertEqual(tile.cant,1)

    def test_tileD(self):
        tile = Tile('D',2,5)
        self.assertEqual(tile.letter,'D')
        self.assertEqual(tile.value,2)
        self.assertEqual(tile.cant,5)


class TestBagTiles(unittest.TestCase):
    @patch ('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        expected_total_tiles = 98
        self.assertEqual(
            bag.total_tiles,
            expected_total_tiles,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1
        )

        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(8)
        self.assertEqual(
            bag.total_tiles,
            90,
            )
    """self.assertEqual(
            len(tiles),
            2,
            )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1),Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            7,
            )"""

if __name__ == '__main__':
    unittest.main()