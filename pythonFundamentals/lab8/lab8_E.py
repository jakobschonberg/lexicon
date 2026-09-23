#E1, E2
class Device:
    def __init__(self, brand, year, is_active = True):
        if year < 0:
            raise ValueError("year cannot be negative")
        self.brand = brand
        self.year = year
        self.is_active = is_active

#E3
class Laptop(Device):
    def __init__(self, brand, year, ram_gb, is_active = True):
        super().__init__(brand, year, is_active)
        self.ram_gb = ram_gb

#E4
class Keyboard(Device):
    def __init__(self, brand, year, layout, is_active = True):
        super().__init__(brand, year, is_active)
        self.layout = layout

laptop = Laptop("Lenovo", 2026, 16)
keyboard = Keyboard("HP", 2008, "sv-SE")

#E5
try:
    antique_laptop = Laptop("Aliens", -1523, 1)    
except Exception as e:
    print(e)

try:
    antique_keyboard = Laptop("Aliens", -3000, "MdC")    
except Exception as e:
    print(e)
