#C1
def greet(name, greeting='Hello'):
    print(greeting, name)

greet("Ada")
greet("Bob", "Good morning")
greet(greeting = "Good evening", name = "Cecil")

#C2
def calculate_price(price, quantity = 1, discount = 0):
    return quantity * price * (1 - discount)

#C3
def create_profice(name, city = 'Unknown', active = True):
    return {"Name": name, "City": city, "Active": active}

d = create_profice("Ada")
print(d["Name"])
print(d["City"])
print(d["Active"])

#C4
greet(greeting = "Good evening", name = "Cecil")

#C5
#greet(greeting = "Good evening", "Cecil") #Positional arguments must appear before keyword arguments
