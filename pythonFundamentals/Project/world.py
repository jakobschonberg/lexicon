import random

tile_types = ["forest", "plains", "hills", "ocean"]

class World:
    world_map = dict()
    player_location = (0, 0)

    def tick():
        px, py = World.player_location
        for x in range(px - 5, px + 6):
            for y in range(py -5, py + 6):
                if (x, y) not in World.world_map.keys:
                    World.generate_tile(x, y)

    def generate_tile(x, y):
        r = random.randint(0, 3)
        tile = Tile(tile_types[r], "", "")
        #Todo add feature generation such as river or town or cave

class Tile:
    def __init__(self, type, features, items):
        self.type = type
        self.features = features
        self.items = items
