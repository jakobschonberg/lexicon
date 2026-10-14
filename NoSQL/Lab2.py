from datetime import datetime
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

#1
for product in db.products.find({"price": {"$gt": 1000}}):
    print(product["name"], product["price"])

#2
for order in db.orders.find({"status": {"$ne": "delivered"}}):
    print(order["_id"], order["status"])

#3
for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
    print(customer["first_name"])

#4
for product in db.products.find({"details.color": "white"}):
    print(product["name"], product["details"])

#5
for product in db.products.find({"tags": "sport"}):
    print(product["name"], product["tags"])

#6
for product in db.products.find({}).sort("price",1).limit(5):
    print(product["name"], product["price"])

#7
for order in db.orders.find({"items.product_id": 2}):
    print(order["_id"])

#8
for product in db.products.find({"category": "Accessories"}):
    print(product["name"], product["category"], product["price"])
db.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}})
for product in db.products.find({"category": "Accessories"}):
    print(product["name"], product["category"], product["price"])

#9
product = db.products.find_one({"name": "Rain Jacket"})
print(product["name"], product["tags"])
db.products.update_one({"name": "Rain Jacket"},
                       {"$push": {"tags": "new"}, "$set": {"restock_date": datetime.now()}})
product = db.products.find_one({"name": "Rain Jacket"})
print(product["name"], product["tags"], product["restock_date"])

#10
print("count:", db.orders.count_documents({"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}}))
result = db.orders.delete_many({"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}})
print("deleted:", result.deleted_count)
print("count:", db.orders.count_documents({"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}}))

