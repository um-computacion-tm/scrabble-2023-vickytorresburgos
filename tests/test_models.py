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

    def test_tileE(self):
        tile = Tile('E',1,12)
        self.assertEqual(tile.letter, 'E')
        self.assertEqual(tile.value,1)
        self.assertEqual(tile.cant,12)

    def test_tileF(self):
        tile = Tile('F',4,1)
        self.assertEqual(tile.letter, 'F')
        self.assertEqual(tile.value,4)
        self.assertEqual(tile.cant,1)

    def test_tileG(self):
        tile = Tile('G',2,2)
        self.assertEqual(tile.letter, 'G')
        self.assertEqual(tile.value,2)
        self.assertEqual(tile.cant,2)

    def test_tileH(self):
        tile = Tile('H',4,2)
        self.assertEqual(tile.letter, 'H')
        self.assertEqual(tile.value,4)
        self.assertEqual(tile.cant,2)

    def test_tileI(self):
        tile = Tile('I',1,6)
        self.assertEqual(tile.letter, 'I')
        self.assertEqual(tile.value,1)
        self.assertEqual(tile.cant,6)
    
    def test_tileJ(self):
        tile = Tile('J',8,1)
        self.assertEqual(tile.letter, 'J')
        self.assertEqual(tile.value,8)
        self.assertEqual(tile.cant,1)

    def test_tileL(self):
            tile = Tile('L',1,4)
            self.assertEqual(tile.letter, 'L')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,4)

    def test_tileLL(self):
            tile = Tile('LL',8,1)
            self.assertEqual(tile.letter, 'LL')
            self.assertEqual(tile.value,8)
            self.assertEqual(tile.cant,1)

    def test_tileM(self):
            tile = Tile('M',3,2)
            self.assertEqual(tile.letter, 'M')
            self.assertEqual(tile.value,3)
            self.assertEqual(tile.cant,2)

    def test_tileN(self):
            tile = Tile('N',1,5)
            self.assertEqual(tile.letter, 'N')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,5)

    def test_tileÑ(self):
            tile = Tile('Ñ',1,5)
            self.assertEqual(tile.letter, 'Ñ')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,5)

    def test_tileO(self):
            tile = Tile('O',1,9)
            self.assertEqual(tile.letter, 'O')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,9)

    def test_tileP(self):
            tile = Tile('P',3,2)
            self.assertEqual(tile.letter, 'P')
            self.assertEqual(tile.value,3)
            self.assertEqual(tile.cant,2)

    def test_tileQ(self):
            tile = Tile('Q',5,1)
            self.assertEqual(tile.letter, 'Q')
            self.assertEqual(tile.value,5)
            self.assertEqual(tile.cant,1)

    def test_tileR(self):
            tile = Tile('R',1,5)
            self.assertEqual(tile.letter, 'R')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,5)

    def test_tileRR(self):
            tile = Tile('RR',8,1)
            self.assertEqual(tile.letter, 'RR')
            self.assertEqual(tile.value,8)
            self.assertEqual(tile.cant,1)

    def test_tileS(self):
            tile = Tile('S',1,6)
            self.assertEqual(tile.letter, 'S')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,6)

    def test_tileT(self):
            tile = Tile('T',1,4)
            self.assertEqual(tile.letter, 'T')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,4)

    def test_tileU(self):
            tile = Tile('U',1,5)
            self.assertEqual(tile.letter, 'U')
            self.assertEqual(tile.value,1)
            self.assertEqual(tile.cant,5)

    def test_tileV(self):
            tile = Tile('V',4,1)
            self.assertEqual(tile.letter, 'V')
            self.assertEqual(tile.value,4)
            self.assertEqual(tile.cant,1)

    def test_tileX(self):
            tile = Tile('X',8,1)
            self.assertEqual(tile.letter, 'X')
            self.assertEqual(tile.value,8)
            self.assertEqual(tile.cant,1)

    def test_tileY(self):
            tile = Tile('Y',4,1)
            self.assertEqual(tile.letter, 'Y')
            self.assertEqual(tile.value,4)
            self.assertEqual(tile.cant,1)

    def test_tileZ(self):
            tile = Tile('Z',10,1)
            self.assertEqual(tile.letter, 'Z')
            self.assertEqual(tile.value,10)
            self.assertEqual(tile.cant,1)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            28,
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
            26,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 10, 1), Tile('Y', 4, 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            30,
        )


if __name__ == '__main__':
    unittest.main()
