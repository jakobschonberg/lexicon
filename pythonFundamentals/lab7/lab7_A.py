#A1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

book1 = Book("The Diamond Throne", "David Eddigs", 496)
book2 = Book("The Silmarillion", "J.R.R. Tolkien", 443)
book3 = Book("2001 A Space Odyssey", "Arthur C. Clarke", 266)
book4 = Book("Daggerspell", "Katharine Kerr", 461)

print(book1.title, book1.author, book1.pages)
print(book2.title, book2.author, book2.pages)
print(book3.title, book3.author, book3.pages)
print(book4.title, book4.author, book4.pages)

#A2
class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Asus", "Vivobook 14", 16, 8392)
laptop2 = Laptop("Acer", "Aspire Lite 15", 8, 7490)
laptop3 = Laptop("Lenovo", "V14 G5", 16, 8738)
laptop1.price = 7290
print(laptop1.brand, laptop1.model, laptop1.ram_gb, laptop1.price)

#A3
laptop4 = Laptop("Lenovo", "V14 G5", 16, 8738)
print(laptop3 is laptop4)

#A4
class Laptop:
    def __init__(self, brand, model, price, ram_gb = 16):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

#A5
laptop = Laptop(model = "Probook 4 G1ah", brand = "HP", price = 9190)
print(laptop.brand, laptop.model, laptop.ram_gb, laptop.price)