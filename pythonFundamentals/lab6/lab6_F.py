import unicodedata
#F1
products = [{"name": "one", "category": "A", "price": 1, "stock": 13},
            {"name": "two", "category": "A", "price": 2, "stock": 14},
            {"name": " three", "category": " B", "price": 3, "stock": 15},
            {"name": "four ", "category": "B", "price": 4, "stock": -16},
            {"name": "Five", "category": "C", "price": 5, "stock": 17},
            {"name": "siX", "category": "C", "price": 6, "stock": -18},
            {"name": "seven", "category": "A", "price": 7, "stock": 0},
            {"name": "eight", "category": "A", "price": 8, "stock": 20},
            {"name": "nine", "category": "B", "price": 9, "stock": 0},
            {"name": "ten", "category": "C", "price": 10, "stock": -22},
            {"name": "elven", "category": "C", "price": 11, "stock": 23},
            {"name": "twelve", "category": "a ", "price": 12, "stock": 24}]

#F2
for product in products:
    product["name"] = unicodedata.normalize('NFD',product["name"].strip().title())
    product["category"] = unicodedata.normalize('NFD',product["category"].strip().title())
    if product["stock"] < 0:
        product["stock"] = 0

for product in products:
    print(product)

#F3
in_stock_products = [product for product in products if product["stock"]]
print("in stock:")
for product in in_stock_products:
    print(product)

#F4
categories = {product["category"] for product in products}
print(categories)

#F5
value_by_product = {d["name"]: d["price"] * d["stock"] for d in products}
for product, value in value_by_product.items():
    print(product, value)

#F6
sorted_by_value = dict(sorted(value_by_product.items(), key=lambda x: x[1], reverse = True))
print(sorted_by_value)

#F7
for rank, product in enumerate(sorted_by_value, start = 1):
    print(rank, product, value_by_product[product])

#F8
ranks = list(range(1,13))
ranked = list(zip(ranks, sorted_by_value, sorted_by_value.values()))
print(ranked)

#F9
import cmath
i = 1j
numbers = [0, 1, 2, 3, 4, 5]
negative_numbers = [-1 * number for number in numbers] #simple, wins because shorter and easier to understand 
print(negative_numbers)
negative_numbers = [round((number * i + cmath.exp(i * cmath.pi) * number).real) for number in numbers] #slightly overcomplicated but we avoided using the minus sign ;)
print(negative_numbers)
