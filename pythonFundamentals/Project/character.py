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
            self.location.items.append(self.items[i])
            del self.items[i]
        
