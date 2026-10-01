from util import clear_screen
from util import wait
from world import World
from world import Location
from bcolors import bcolors
from combat import do_combat

class MenuItem:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class MainMenu:
    def __init__(self, menu_items = None):
        if menu_items == None:
            self.menu_items = []
        else:
            self.menu_items = menu_items

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

    def remove_item(self, menu_item_id):
        del self.menu_items[menu_item_id]

def display(location):
    clear_screen()
    print(f"{bcolors.BLUE}{location.name}{bcolors.END}")
    print(location.description)
    if location.has_hostiles():
        do_combat()
    if len(location.items):
        print(bcolors.GREEN)
        for item in location.items:
            print(item.name)
        print(bcolors.END)
        print(f"{bcolors.ORANGE}P{bcolors.END} - pick up item") 
    exits = {}
    for num, exit in enumerate(location.exits, start = 1):
        print(f"{bcolors.ORANGE}{num}{bcolors.END}. {exit.name}")
        exits[num] = exit
    print(f"{bcolors.ORANGE}I{bcolors.END} - Inventory")
    i = None
    while True:
        try:
            i = input()
            if (i.lower() == 'i'):
                return "inventory"
            elif (i.lower() == 'p' and len(location.items)):
                return "pickup"
            i = int(i)
            if i in exits.keys():
                return exits[i].target_location
        except Exception as e:
            if e is EOFError:
                break

def show_inventory():
    clear_screen()
    player_items = {}
    has_wieldable_items = False
    for num, item in enumerate(World.player.items, start = 1):
        print(f"{bcolors.ORANGE}{num}{bcolors.END}", item.display_name())
        player_items[num] = item
        if item.is_wieldable():
            has_wieldable_items = True
    if len(player_items):
        print (f"{bcolors.ORANGE}D{bcolors.END} - Drop item")
        print (f"{bcolors.ORANGE}U{bcolors.END} - Use item")
        if has_wieldable_items:
            print (f"{bcolors.ORANGE}E{bcolors.END} - Equip/Unequip item")
        print (f"{bcolors.ORANGE}Enter{bcolors.END} - Continue")
        i = input().lower()
        if i == 'd':
            try: 
                id = int(input("Drop which item? "))
                if id in player_items.keys():
                    World.player.drop_item(id - 1)
            except Exception as e:
                pass
        elif i == 'e':
            try: 
                id = int(input("Equip/unequip which item? "))
                if id in player_items.keys():
                    World.player.equip(id - 1)
            except Exception as e:
                pass
        elif i == 'u':
            raise NotImplementedError
    else:
        print("Your inventory is empty.")
        print("-continue-")
        wait()

def pick_up_item():
    clear_screen()
    items = {}
    for num, item in enumerate(World.player.location.items, start = 1):
        print(f"{bcolors.ORANGE}{num}{bcolors.END}", item.name)
        items[num] = item
    i = input("Pick up which item?")
    try:
        id = int(i)
        if id in items.keys():
            World.player.pick_up_item(id - 1)
    except Exception as e:
        pass

def new_game():
    location = World.player.location
    while location:
        result = display(location)
        if isinstance(result, str):
            if result == "inventory":
                show_inventory()
            elif result == "pickup":
                if World.player.inventory_space() > 0:
                    pick_up_item()
                else:
                    print("No free inventory space")
                    wait()
        elif isinstance(result, Location):
            location = result
            World.player.location = location    

menu = MainMenu([
    MenuItem("Start New Game", "new"),
    MenuItem("Quit Game", "quit")
])

choice = None
while choice is None:
    clear_screen()
    for num, item in enumerate(menu.menu_items, start = 1):
        print(f"{bcolors.ORANGE}{num}{bcolors.END}. {item.name}")

    try:
        choice = int(input()) - 1
        if choice < 0 or choice >= len(menu.menu_items):
            choice = None
            raise(ValueError)
    except Exception as e:
        pass #print(e)

chosen = menu.menu_items[choice].id
if chosen == "new":
    new_game()
elif chosen == "quit":
    print("Goodbye")


