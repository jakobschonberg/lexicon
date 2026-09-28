class Character:
    def __init__(self, base_combat_strength, max_health, name, items):
        self.base_combat_strength = base_combat_strength
        self.max_health = max_health
        self.health = max_health
        self.name = name
        if items == None:
            self.items = []
        else:
            self.items = items
        
