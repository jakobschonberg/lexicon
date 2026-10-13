from datetime import datetime
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

#1
for product in db.products.find({"category": "Accessories"}):
    print(product["name"])

#2
for customer in db.customers.find({"city": "Göteborg"}):
    print(customer["first_name"], customer["last_name"])

#3
for product in db.products.find():
    print(product["name"], product["price"])

#4
print(db.customers.count_documents({"city": "Uppsala"}))

#5
product = db.products.find_one({"name": "Sandals"})
print(product["stock"])

#6
for customer in db.customers.find({"newsletter": True}):
    print(customer["first_name"])

#7
customer = {"first_name": "Jakob",
            "last_name": "Schönberg",
            "email": "me@spam.com",
            "city": "Täby",
            "joined": datetime.now(),
            "newsletter": False}
#db.customers.insert_one(customer)

#8
product1 = {"_id": 13,
            "name": "USB stick",
            "category": "Electronics",
            "price": "100",
            "stock": 10,
            "tags": [],
            "details": {"size": "16 Gb", "color": "black"}}
product2 = {"_id": 14,
            "name": "Dolphins cap",
            "category": "Accessories",
            "price": "100",
            "stock": 2,
            "tags": [],
            "details": {"size": "large", "color": "teal"}}
#db.products.insert_many([product1, product2])

#9
for customer in db.customers.find():
    print(customer["first_name"], customer["last_name"], dict.get(customer, "city", "(unknown)"))

#10
for order in db.orders.find():
    print(f'Order {order["_id"]}: {len(order["items"])} items')
