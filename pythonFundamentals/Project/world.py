#import random
from character import Character
from character import Character_Type
from item import Item, Item_Type

#tile_types = ["forest", "plains", "hills", "ocean"]

class Exit:
    def __init__(self, name, target_location):
        self.name = name
        self.target_location = target_location

class Location:
    def __init__(self, name, type, characters, items, exits, description):
        self.name = name
        self.type = type
        self.characters = characters
        self.items = items
        self.exits = exits
        self.description = description
        for character in self.characters:
            character.location = self

    def has_hostiles(self):
        for character in self.characters:
            if character.character_type == Character_Type.enemy:
                return True
        return False

short_bow = Item("Short bow", Item_Type.weapon, 2, True)

goblin_archer = Character(7, 14, Character_Type.enemy, "Goblin archer", [short_bow])

location_3 = Location("Ruin", "plains", [goblin_archer], [], [],
                      "You come upon a ruined building. You go closer to investigate when suddenly an arrow flies by your ear." \
                      "You turn your head and see a goblin reaching for another arrow. You have no choice but to engage in the fight."
                      )

exit_2_to_3 = Exit("Ruin", location_3)

small_backpack = Item("Small backpack", "bag", 0)
short_sword = Item("Short sword", "weapon", 2)
dagger = Item("Dagger", "weapon", 1)
goblin_armor = Item("Goblin armor", "misc", 0)

location_2 = Location("Battlefield", "plains", [], [small_backpack, short_sword, dagger, goblin_armor], [exit_2_to_3],
                      "As you exit the forest into a large open field, something smells really bad.\n" \
                      "Looking further ahead you notice signs of recent battle. Goblin corpses lie mixed\n" \
                      "with halfling corpses. Besides some vulture birds, nobody seems to be around.\n" \
                      "You can loot the corpses if you wish."
                      )
exit_1_to_2 = Exit("East", location_2)
berries = Item("Red berrries", "food", 0)
mushrooms = Item("Mushrooms", "food", 0)

location_1 = Location("Forest", "forest", [], [berries, mushrooms], [exit_1_to_2],
                      "You manage to make your way into the forest, the tall trees provide a welcome shade from the sun,\n" \
                      "but you realize you are very hungry.\n" \
                      "You see some red berries as well as some suspisious looking mushrooms. You don't have any bag or\n" \
                      "backpack to collect food, but you could try and eat some."                      
                      )

exit_start_to_1 = Exit("Forest", location_1)

start_location = Location("Unkown beach", "beach", [], [], [exit_start_to_1],
                          "You wake up disoriented...\n" \
                          "You don't recall how you got here, but you seem to be just at the beach,\n" \
                          "just meters away from the ocean. The sun is blasting you from above.\n" \
                          "You look around but see nothing else of note. You decide to get up and head for shelter\n" \
                          "in a nearby forest. Judging by the the sun's position you estimate the forest is to the south."
                          )



class World:
    world_map = dict()
    rags = Item("Rags", Item_Type.armor, 0, True)
    player = Character(10, 20, Character_Type.player, "Player", [rags])
    player.location = start_location

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



