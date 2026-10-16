from pymongo import MongoClient
import json
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

#1
'''
Reference the reviews. As they can grow endlessy, it could become a problem if we embed them.
'''

#2
'''
Advantage: We don't need another query to get the product name when fetching order info.
Disadvantage: Storing the name is a waste of space (we only need to store the id)
'''

#3
newsletter_validation =  {
    "$jsonSchema": {
        "bsonType": 'object',
        "required": [
            '_id',
            'email',
            'source'
        ],
        "properties": {
            "_id": {
                "bsonType": 'objectId'
            },
            "email": {
                "bsonType": 'string',
                "pattern": '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
            },
            "source": {
                "bsonType": "string",
                "enum": ["web", "store"]
            }
        }
    }
}
try:
    db.newsletter_signups.drop()
    db.create_collection("newsletter_signups", validator=newsletter_validation)
    db.newsletter_signups.insert_one({"email": "me@spam.com", "source": "web"})
    #db.newsletter_signups.insert_one({"email": "someone@spam.com", "source": "trust me"})
except Exception as e:
    print(e)
'''
Document failed validation, full error: {'index': 0, 'code': 121, 'errmsg': 'Document failed validation',
    'errInfo': {'failingDocumentId': ObjectId('6ad1e1f73414e27ece913dda'), 'details': {'operatorName': '$jsonSchema', 'schemaRulesNotSatisfied': [{'operatorName': 'properties', 'propertiesNotSatisfied': [{'propertyName': 'source', 'details': [{'operatorName': 'enum', 'specifiedAs': {'enum': ['web', 'store']},
    'reason': 'value was not found in enum', 'consideredValue': 'trust me'}]}]}]}}}
'''

#4
results = db.customers.aggregate([{"$group": {"_id": "$city", "count": {"$sum": 1}}},
                                          {"$sort": {"count": -1}}
                                          ])
for aggregate in results:
    print(f'{str(aggregate.get("_id", "(unknown)")):<20} {aggregate.get("count", "0")}')

#5
results = db.products.aggregate([{"$group": {"_id": "$category",
                                             "cheapest": {"$min": {"min_price": "$price", "min_product": "$name"}},
                                             "most_expensive": {"$max": {"max_price": "$price", "max_product": "$name"}}
                                 }}])
for aggregate in results:
    print(f'{aggregate["_id"]:<15} cheapest: {aggregate["cheapest"]["min_product"]:<15}{aggregate["cheapest"]["min_price"]:>4}     most expensive: {aggregate["most_expensive"]["max_product"]:<15}{aggregate["most_expensive"]["max_price"]:>4}')

#6
results = db.orders.aggregate([{"$group": {"_id": "$customer_id","count": {"$sum": 1}}},
                                {"$match": {"count": {"$gte": 2}}},
                                {"$sort": {"count": -1}}
                            ])
for aggregate in results:
    print(f'customer {aggregate["_id"]}: {aggregate["count"]} orders')

#7
results = db.orders.aggregate([{"$project": {"_id": "$_id", "count": {"$sum": {"$size": "$items"}}}}])
for aggregate in results:
    print(f'{aggregate["_id"]} {aggregate["count"]}')

#8
results = db.orders.aggregate([{"$match": {"status": {"$ne": "cancelled"}}},
                               {"$unwind": "$items"},
                               {"$lookup": {"from": "products", "localField": "items.product_id", "foreignField": "_id", "as": "product"}},
                               {"$unwind": "$product"},                               
                               {"$group": {"_id": "$product.category", "count": {"$sum": "$items.quantity"}}}
                            ])
for aggregate in results:
    print(f'{aggregate["_id"]:<15} {aggregate["count"]:>2}')

#9
results = db.orders.aggregate([{"$unwind": "$items"},
    {"$group": {"_id": "$status", "count": {"$sum": {"$multiply": ["$items.quantity", "$items.unit_price"]}}}}])
for aggregate in results:
    print(f'{aggregate["_id"]:<15} {aggregate["count"]:>2}')

#10
results = db.products.aggregate([{"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}])
for aggregate in results:
    print(f'{aggregate["_id"]:<15} {aggregate["count"]:>2}')

#11
def find_orders(request_text):
    data = json.loads(request_text)
    return list(db.orders.find({"status": data["status"]}))
'''
The 2nd call returns all items where status is not equal to 'x'
instead of getting items where status is the given string
'''
def find_orders(request_text):
    data = json.loads(request_text)
    return list(db.orders.find({"status": str(data["status"])}))

for order in find_orders('{"status": "new"}'):
    print(order["_id"])
print("---")
for order in find_orders('{"status": {"$ne": "x"}}'):
    print(order["_id"])

#12
def products_under(text):
    try:
        floating_value = float(text)
        return db.products.aggregate([{"$match": {"price": {"$lt": floating_value}}},
                                      {"$project": {"name": "$name", "price": "$price"}}])
    except Exception as e:
        print("Please enter a number.")
        return []

for product in products_under("300"):
    print(f'{product["name"]:<20} {product["price"]}')
for product in products_under("abc"):
    print(f'{product["name"]:<20} {product["price"]}')
for product in products_under('{"$gt": 0}'):
    print(f'{product["name"]:<20} {product["price"]}')

#13
client2 = MongoClient("mongodb://localhost:27018/", serverSelectionTimeoutMS=2000, connectTimeoutMS=2000, socketTimeoutMS=2000)
db2 = client2["webshop"]
try:
    print(db2.products.count_documents({}))
except Exception as e:
    print("Unable to connect to MongoDB")
'''
program waits until time out and eventually throws error 'pymongo.errors.ServerSelectionTimeoutError'
'''
try:
    print(db.products.count_documents({}))
except Exception as e:
    print("Unable to connect to MongoDB")

#14
'''
ALl fields. Although some fields by themselves do not say much, in combination with other fields
it might say more than it would without the field.
When a customer is deleted, the orders remain. Since only customer_id is kept, a minimum
of personal data is kept. Orders can technically be deleted after a set number of years if laws allow it, but not before that.
Copying personal data into the order is not adviced, since orders have to be kept for years, it makes cleaning up personal data more difficult.
Is the gain of speed absolutely needed? And if so do we correctly clean up all personal data if a customer wants to be deleted?
'''