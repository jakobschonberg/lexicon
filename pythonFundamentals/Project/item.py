from enum import Enum

class Item_Type(Enum):
    armor = 1
    weapon = 2
    food = 3
    misc = 4

class Item:
    def __init__(self, name, item_type, combat_score, wielded = False):
        self.name = name
        self.item_type = item_type
        self.combat_score = combat_score
        self.wielded = wielded