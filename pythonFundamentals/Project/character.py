class Character:
    def __init__(self, base_combat_strength, max_health, name, location, items):
        self.base_combat_strength = base_combat_strength
        self.max_health = max_health
        self.health = max_health
        self.name = name
        self.location = location
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
                item.wielded = not item.wielded
            else:
                print(f"{item.name} cannot be equipped")
        
