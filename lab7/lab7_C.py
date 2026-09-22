#C1, C2, C3
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    tax_rate = .12

    def price_with_tax(self):
        return round(self.price * (1 + self.tax_rate), 2)

#C4
product1 = Product("Cola", 14)
product2 = Product("Fries", 19)
product3 = Product("Burger", 33)
print(product1.name, product1.price_with_tax())
print(product2.name, product2.price_with_tax())
print(product3.name, product3.price_with_tax())

#C5
Product.tax_rate = .06
print(product1.name, product1.price_with_tax())
print(product2.name, product2.price_with_tax())
print(product3.name, product3.price_with_tax())

#C6
product1.tax_rate = .25
print(product1.tax_rate, product2.tax_rate, Product.tax_rate)
