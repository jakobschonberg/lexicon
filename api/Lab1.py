import requests
from time import sleep

#3
from api_client import get_json

#1
products = get_json("https://fakestoreapi.com/products")
for item in sorted(products, key= lambda x: x["price"]):
    print(f"{item["price"]} - {item["title"]}")

#2
sleep(0.2)
categories = get_json("https://fakestoreapi.com/products/categories")
if categories is not None:
    for item in categories:
        print(item)
    category = None
    while(category == None):
        category = input("Get count of products for which category? ")
        if (category not in categories):
            category = None
    sleep(0.2)
    products = get_json("https://fakestoreapi.com/products/category/" + category)
    print(f"{len(products)} products in category {category}")

#4
sleep(0.2)
new_product = {
    "title": "some product",
    "price": "67",
    "description": "This product is somewhat of a joke",
    "image": "https://imgs.xkcd.com/comics/funny_numbers.png",
    "category": "men's clothing"
}
response = requests.post('https://fakestoreapi.com/products', json=new_product, timeout=5)
print(response.status_code)
print(response.json())
sleep(0.2)
response = requests.patch('https://fakestoreapi.com/products/7', json={"price": 67}, timeout=5)
print(response.status_code)
print(response.json())

#5
sleep(0.2)
response = get_json("https://www.google.com/")
if response is not None:
    print(response)
sleep(0.2)
response = get_json('https://fakestoreapi.com/products', timeout=0.001)
if response is not None:
    print(response)
sleep(0.2)
response = get_json('This is not a valid URL')
if response is not None:
    print(response)


