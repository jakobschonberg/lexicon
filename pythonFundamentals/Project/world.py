#import random
from character import Character
from item import Item, Item_Type

#tile_types = ["forest", "plains", "hills", "ocean"]

class Location:
    def __init__(self, name, type, features, items, exits, description):
        self.name = name
        self.type = type
        self.features = features
        self.items = items
        self.exits = exits
        self.description = description
        

start_location = Location("Unkown beach", "beach", [], [],
                          "You wake up disoriented..." \
                          "You don't recall how you got here, but you seem to be just at the beach," \
                          "just meters away from the ocean. The sun is blasting you from above." \
                          "You look around but see nothing else of note. You decide to get up and head for shelter" \
                          "in a nearby forest."
                          )

class World:
    world_map = dict()
    player_location = start_location
    rags = Item("Rags", Item_Type.armor, 0, True)
    player = Character(10, 20, "Player", [rags])

    # def tick():
    #     px, py = World.player_location
    #     for x in range(px - 5, px + 6):
    #         for y in range(py -5, py + 6):
    #             if (x, y) not in World.world_map.keys:
    #                 World.generate_tile(x, y)

    # def generate_tile(x, y):
    #     r = random.randint(0, 3)
    #     tile = Tile(tile_types[r], "", "")
    #     #Todo add feature generation such as river or town or cave



