from util import clear_screen
from util import wait
from world import World
from world import Location
#from item import Item
from bcolors import bcolors
#import win32gui

#current_window = win32gui.GetForegroundWindow()
#win32gui.MoveWindow(current_window. 100, 100, 640, 480)

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
    exits = {}
    for num, exit in enumerate(location.exits, start = 1):
        print(f"{num}. {exit.name}")
        exits[num] = exit
    i = None
    while True:
        try:
            i = input()
            if (i.lower() == 'i'):
                return "inventory"
            i = int(i)
            if i in exits.keys():
                return exits[i].target_location
        except Exception as e:
            if e is EOFError:
                break

def show_inventory():
    clear_screen()
    items = {}
    for num, item in enumerate(World.player.items, start = 1):
        print(num, item.name)
        items[num] = item
    if len(items):
        print ("D - Drop item")
        print ("U - Use item")
        print ("Any other key - Continue")
        i = input().lower()
        if i == 'd':
            try: 
                id = int(input("Drop which item?"))
                if id in items.keys():
                    World.player.drop_item(id - 1)
            except Exception as e:
                pass
        if i == 'u':
            raise NotImplementedError
    else:
        print("Your inventory is empty.")
        print("-continue-")
        wait()

def new_game():
    location = World.player.location
    while location:
        result = display(location)
        if isinstance(result, str) and result == "inventory":
            show_inventory()
        elif isinstance(result, Location):
            location = result
            World.player.location = location

    
    

def load():
    raise NotImplementedError()

menu = MainMenu([
    MenuItem("Start New Game", "new"),
    MenuItem("Load Game", "load"),
    MenuItem("Quit Game", "quit")
])

choice = None
while choice is None:
    clear_screen()
    for num, item in enumerate(menu.menu_items, start = 1):
        print(f"{num}. {item.name}")

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
elif chosen == "load":
    load()
elif chosen == "quit":
    print("Goodbye")


