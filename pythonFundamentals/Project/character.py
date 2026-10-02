from enum import Enum
from item import Item_Type
from util import wait
from util import clear_screen
from time import sleep
from bcolors import bcolors
from item import Item

class Character_Type(Enum):
    player = 1
    npc = 2
    enemy = 3

class Character:
    def __init__(self, base_combat_strength: int, max_health: int, character_type: Character_Type, name: str, items: list[Item]):
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

    def drop_item(self, i) -> None:
        if i >= 0 and i < len(self.items):
            self.items[i].wielded = False
            self.location.items.append(self.items[i])
            del self.items[i]
        if self.inventory_space() < 0: #if we drop a bag, we might have negative free inventory space, so we might drop more items
            index_to_be_dropped = 0
            for index, item in enumerate(self.items):
                if item.item_type != Item_Type.bag and (item.item_type != Item_Type.armor or not item.wielded):
                    index_to_be_dropped = index
            self.drop_item(index_to_be_dropped)
            

    def use_item(self, i) -> None:
        if i >= 0 and i < len(self.items):
            if self.items[i].item_type == Item_Type.food:
                self.health = min(self.max_health, self.health + self.items[i].score)
                if self.character_type == Character_Type.player:
                    print(f"You eat {self.items[i].name}")
                    sleep(2)
                    if self.items[i].score < 0:
                        print(f"{bcolors.RED}You don't feel so good{bcolors.END}")
                    elif self.items[i].score > 0:
                        print(f"{bcolors.GREEN}You feel refreshed{bcolors.END}")
                    sleep(2)
                del self.items[i]
                if self.health <= 0:
                    self.kill(True)
                

    def pick_up_item(self, i) -> None:
        if i >= 0 and i < len(self.location.items):
            self.items.append(self.location.items[i])
            del self.location.items[i]

    def equip(self, i) -> None:
        if i >= 0 and i < len(self.items):
            item = self.items[i]
            if item.is_wieldable():
                item_name = item.name
                item.wielded = not item.wielded
                if not item.wielded and self.inventory_space() < 0:
                    self.drop_item(i)
                    print(f"Your invntory is full, so you dropped {item_name}")
                    wait()
                if item.wielded: #Can only equip 1 armor and 1 weapon at a time
                    if item.item_type == Item_Type.armor or item.item_type == Item_Type.weapon:
                        for other_item in self.items:
                            if other_item != item and other_item.item_type == item.item_type:
                                other_item.wielded = False
            else:
                print(f"{item.name} cannot be equipped")
                wait()

    def combat_strength(self) -> int:
        strength = self.base_combat_strength
        for item in self.items:
            if item.wielded:
                strength += item.score
        return strength

    def kill(self, clear = False) -> None:
        if self.character_type == Character_Type.player:
            sleep(1)
            if clear:
                clear_screen()
            print(f"Health: {self.health} / {self.max_health}")
            print(f"Game over - {bcolors.DARKRED}You have died{bcolors.END}.")
            self.location = None
        else:
            print(f"{self.name} dies")
            while len(self.items):
                self.drop_item(0)
            for index, character in enumerate(self.location.characters):
                if character == self:
                    del self.location.characters[index]

    def inventory_space(self) -> int:
        space = 2
        for item in self.items:
            if item.item_type == Item_Type.bag:
                space += 4
            elif item.item_type != Item_Type.armor or not item.wielded:
                space -= 1
        return space

    def max_inventory_space(self) -> int:
        space = 2
        for item in self.items:
            if item.item_type == Item_Type.bag:
                space += 5
        return space
