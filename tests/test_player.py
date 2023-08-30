import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):
    def __init__(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

if __name__ == '__main__':
    unittest.main()