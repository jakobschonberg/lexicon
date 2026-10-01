from character import Character
from character import Character_Type
from item import Item, Item_Type

class Exit:
    def __init__(self, name, target_location):
        self.name = name
        self.target_location = target_location

class Location:
    def __init__(self, name, type, characters, items, description, revisit_description = ""):
        self.name = name
        self.type = type
        self.characters = characters
        self.items = items
        self.exits = []
        self.description = description
        self.revisit_description = revisit_description
        for character in self.characters:
            character.location = self

    def has_hostiles(self):
        for character in self.characters:
            if character.character_type == Character_Type.enemy:
                return True
        return False


start_location = Location("Unkown beach", "beach", [], [],
                          "You wake up disoriented...\n" \
                          "You don't recall how you got here, but you seem to be just at the beach,\n" \
                          "just meters away from the ocean. The sun is blasting you from above.\n" \
                          "You look around but see nothing else of note. You decide to get up and head for shelter\n" \
                          "in a nearby forest. Judging by the the sun's position you estimate the forest is to the south.",
                          "You are at the beach. There is a forest to the south."
                          )


berries = Item("Red berrries", Item_Type.food, 3)
mushrooms = Item("Mushrooms", Item_Type.food, -50)

location_1 = Location("Forest", "forest", [], [berries, mushrooms],
                      "You manage to make your way into the forest, the tall trees provide a welcome shade from the sun,\n" \
                      "but you realize you are very hungry.\n" \
                      "You see some red berries as well as some suspisious looking mushrooms.",
                      "You are in a forest. The tall trees provide a welcome shade from the sun."
                      )


small_backpack = Item("Small backpack", Item_Type.bag, 0)
short_sword = Item("Short sword", Item_Type.weapon, 2)
dagger = Item("Dagger", Item_Type.weapon, 1)
goblin_armor = Item("Goblin armor", Item_Type.armor, 1)

location_2 = Location("Battlefield", "plains", [], [small_backpack, short_sword, dagger, goblin_armor],
                      "As you exit the forest into a large open field, something smells really bad.\n" \
                      "Looking further ahead you notice signs of recent battle. Goblin corpses lie mixed\n" \
                      "with halfling corpses. Other than some vulture birds, nobody seem to be around.\n" \
                      "You can loot the corpses if you wish.",
                      "You are at the battlefield. Goblin corpses lie mixed with halfling corpses.\n" \
                      "Other than some vulture birds, nobody seem to be around."
                      )


short_bow = Item("Short bow", Item_Type.weapon, 2, True)
goblin_archer = Character(7, 14, Character_Type.enemy, "Goblin archer", [short_bow])

location_3 = Location("Ruin", "plains", [goblin_archer], [],
                      "You come upon a ruined building. You go closer to investigate when suddenly an arrow flies by your ear.\n" \
                      "You turn your head and see a goblin reaching for another arrow. You have no choice but to engage in the fight.",
                      "You are in the ruined building."
                      )
bear = Character(20, 30, Character_Type.enemy, "Angered Bear", [])

location_4 = Location("Cave", "cave", [bear], [],
                      "You step inside the cave, but it's not empty. An angry bear attacks you. You must defend yourself.")


start_location.exits.append(Exit("Forest", location_1))
location_1.exits.append(Exit("Beach", start_location))
location_1.exits.append(Exit("East", location_2))
location_2.exits.append(Exit("West", location_1))
location_2.exits.append(Exit("Ruin", location_3))
location_2.exits.append(Exit("Cave", location_4))
location_3.exits.append(Exit("Battlefield", location_2))
location_4.exits.append(Exit("Battlefield", location_2))

class World:
    world_map = dict()
    rags = Item("Rags", Item_Type.armor, 0, True)
    player = Character(10, 20, Character_Type.player, "Player", [rags])
    player.location = start_location



