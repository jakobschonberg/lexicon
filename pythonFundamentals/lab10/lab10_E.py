#E1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#E2
product = Product("ball", 5)
print(product)

#E3
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.price}"

#E4
product1 = Product("ball", 5)
product2 = Product("dice", 7)
product3 = Product("cube", 10)

print(product1)
print(product2)
print(product3)

#E5
s = str(product1)
print(type(s))