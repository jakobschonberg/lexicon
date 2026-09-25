from util import clear_screen

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