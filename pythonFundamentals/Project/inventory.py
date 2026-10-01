from util import clear_screen
from util import wait
from bcolors import bcolors
from world import World

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
            try: 
                id = int(input("Use which item? "))
                if id in player_items.keys():
                    World.player.use_item(id - 1)
            except Exception as e:
                pass
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