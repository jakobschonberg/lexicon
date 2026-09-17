# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
total_value = 0
max_product = None
max_price = None
print("In stock products:")
for product in products:
    if(product["stock"]):
        print(product["name"])
        total_value += product["stock"] * product["price"]
        if not max_price or product["price"] > max_price:
            max_price = product["price"]
            max_product = product["name"]
print("Total value:",total_value)
print("Highest price in-stock product:", max_product)


# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average(scores):
    return sum(scores)/len(scores)

def create_result(scores):
    if calculate_average(scores) >= 70:
        return "PASS"
    return "FAIL"

print(calculate_average(scores), create_result(scores))

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:
def calculate_order(customer_name, *product_prices, **settings):
    subtotal = sum(product_prices)
    discount = 0
    shipping = 0
    if "discount" in settings.keys():
        discount = settings["discount"]
    if "shipping" in settings.keys():
        shipping = settings["shipping"]
    final_total = subtotal * (1 - discount / 100) + shipping
    r = {}
    r["customer"] = customer_name
    r["subtotal"] = subtotal
    r["final_total"] = final_total
    r["settings"] = settings
    return r

print(calculate_order("Anna", *product_prices, **order_settings))

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
normalized_player_names = [player["name"].strip().title() for player in players]
print("normalized names:", normalized_player_names)
active_players = [player["name"].strip().title() for player in players if player["active"] and player["score"] >= 80]
print("active players:", active_players)
sorted_players = sorted(players, key = lambda x: x["score"], reverse = True)
for num, player in enumerate(sorted_players, start = 1):
    print(f"{num}. {player["name"].strip().title()} - {player["score"]}")
scores = [player["score"] for player in players]
names_and_scores = zip(normalized_player_names, scores)
for name, score in names_and_scores:
    print(name, score)
