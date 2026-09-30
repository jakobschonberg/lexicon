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

    def display_name(self):
        if self.item_type == Item_Type.armor and self.wielded:
            return f"{self.name} (worn)"
        if self.item_type == Item_Type.weapon and self.wielded:
            return f"{self.name} (wielded)"
        return self.name

    def is_wieldable(self):
        if self.item_type == Item_Type.armor or self.item_type == Item_Type.weapon:
            return True
        return False
        