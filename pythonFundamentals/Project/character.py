from enum import Enum
from item import Item_Type
from util import wait

class Character_Type(Enum):
    player = 1
    npc = 2
    enemy = 3

class Character:
    def __init__(self, base_combat_strength, max_health, character_type, name, items):
        self.base_combat_strength = base_combat_strength
        self.max_health = max_health
        self.character_type = character_type
        self.health = max_health
        self.name = name
        self.location = None #To avoid cycle dependancies Charcter Location is either set seperately or upon Location creation
        if items == None:
            self.items = []
        else:
            self.items = items

    def drop_item(self, i):
        if i >= 0 and i < len(self.items):
            self.items[i].wielded = False
            self.location.items.append(self.items[i])
            del self.items[i]

    def pick_up_item(self, i):
        if i >= 0 and i < len(self.location.items):
            self.items.append(self.location.items[i])
            del self.location.items[i]

    def equip(self, i):
        if i >= 0 and i < len(self.items):
            item = self.items[i]
            if item.is_wieldable():
                item_name = item.name
                item.wielded = not item.wielded
                if not item.wielded and self.inventory_space() < 0:
                    self.drop_item(i)
                    print(f"Your invntory is full, so you dropped {item_name}")
                    wait()
            else:
                print(f"{item.name} cannot be equipped")
                wait()

    def combat_strength(self):
        strength = self.base_combat_strength
        for item in self.items:
            if item.wielded:
                strength += item.score
        return strength

    def kill(self):
        while len(self.items):
            self.drop_item(0)
        for index, character in enumerate(self.location.characters):
            if character == self:
                del self.location.characters[index]

    def inventory_space(self):
        space = 2
        for item in self.items:
            if item.item_type == Item_Type.bag:
                space += 4
            elif item.item_type != Item_Type.armor or not item.wielded:
                space -= 1
        return space
