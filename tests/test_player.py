import unittest
from game.player import Player,NoLetterException
from game.bagtiles import BagTiles
from game.tiles import Tile
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,   
        )
        self.assertEqual(player_1.score,0)
    def test_get_score(self):
        player=Player()
        score=player.get_score()
        print(score)
        self.assertEqual(score,0)
    def test_get_tiles(self):
        player=Player()
        tiles=player.get_tiles()
        self.assertEqual(tiles,[])    
    def test_take_tiles_from_the_bag(self):
        Player1=Player()
        bag=BagTiles()
        Player1.take_tiles_from_the_bagtiles(bag,2)
        self.assertEqual(len(Player1.tiles),2)        
    def test_player_exchange(self):
        player = Player()
        bag = BagTiles()
        player.take_tiles_from_the_bagtiles(bag, 2)
        tile = player.tiles[0]
        player.exchange_tile(bag,player.tiles[0])
        self.assertFalse(tile == player.tiles[0])    
    def test_find_letter_in_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 1)]
        letra = player.find_letter_in_tiles('B')
        self.assertEqual(letra,"B")
    def test_not_find_letter_in_tiles(self):
        player=Player()
        player.tiles=[Tile('A', 1), Tile('B', 3), Tile('C', 1)] 
        resultado=player.find_letter_in_tiles("x")
        self.assertEqual(resultado,None)    
    def test_give_requested_tiles(self):
        player=Player()
        player.tiles=  [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]  
        valid=player.give_requested_tiles('HOLA')
        list=['H','O','L','A']
        self.assertEqual(valid,list)  
    def test_not_give_request_tiles(self):
        player=Player() 
        player.tiles=  [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]       
        with self.assertRaises(NoLetterException):
         player.give_requested_tiles('holas')
  
    def test_get_name (self):
        player=Player()
        player.name="emi"
        self.assertEqual(player.get_name(),"emi")   
    def test_set_name (self):
        player=Player()
        player.set_name("emi")
        self.assertEqual(player.get_name(),"emi") 
    def test_show_tiles(self):
        player=Player()
        player.tiles=["A","B"]
        self.assertEqual(player.show_tiles(),["A","B"])  
    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)

    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=3),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        

        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, False)
        
    def test_validate_user_has_letters_2(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = "HOLA"
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)
        
    def test_validate_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='S', value=4),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = [
            Tile(letter='C', value=3),
            Tile(letter='A', value=1),
            Tile(letter='S', value=4),
            Tile(letter='A', value=1),
        ]
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, False)
        
    def test_validate_user_has_not_word(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=4),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=3),
            Tile(letter='U', value=1),
            Tile(letter='M', value=3),
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = "WAPA"
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, False)

    def test_validate_user_has_letters_3(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='C', value=4),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),
            Tile(letter='A', value=1),
            
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = [
            Tile(letter='C', value=4),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),
            Tile(letter='A', value=1),
        ]
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)
        
    def test_validate_user_has_letters_4(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='C', value=4),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),
            Tile(letter='A', value=1),
            
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = "CASA"
        
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)  
    def test_validate_user_has_letters_in_list(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=4),
            Tile(letter='E', value=1),
            Tile(letter='RR', value=8),
            Tile(letter='E', value=1),
            
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = ["P","E","RR","E"]
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)
        
    def test_validate_user_has_letters_in_list_2(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=4),
            Tile(letter='E', value=1),
            Tile(letter='RR', value=8),
            Tile(letter='O', value=1),
            
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = ["P","E","RR","O"]
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, True)
        
    def test_validate_user_has_letters_in_list_false(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=4),
            Tile(letter='I', value=1),
            Tile(letter='LL', value=8),
            Tile(letter='A', value=1),
            
        ]
        player_1 = Player()
        for i in bag_tile.tiles:
            player_1.tiles.append(i)
        tiles = ["P","E","RR","O"]
        is_valid = player_1.has_letters(tiles)
        
        self.assertEqual(is_valid, False)   
    def test_remove_tile(self):
        player = Player()
        player.tiles = [
            Tile(letter='C', value=4),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),
            Tile(letter='A', value=1),
        ]
        player.remove_tile(Tile("A",1))
        self.assertEqual(len(player.tiles),3)
        
    def test_add_tile(self):
        player = Player()
        player.tiles = [
            Tile(letter='C', value=4),
            Tile(letter='A', value=1),
            Tile(letter='S', value=1),
            Tile(letter='A', value=1),
        ]
        player.add_tile(Tile("A",1))
        self.assertEqual(len(player.tiles),5)
if __name__ == '__main__':
    unittest.main()