class Player:
    def __init__(self, bag_tiles):
        self.tiles = bag_tiles.take(7)
        self.bag_tiles = bag_tiles
    
    def rellenar(self):
        self.tiles += bag_tiles.take