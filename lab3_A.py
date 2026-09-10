#A1
numbers = [-1, "banana", 0, 2, 3.5]
for number in numbers:
    if type(number) != int and type(number) != float:
        print(f"{number} is not a number")
    elif number < 0:
        print(f"{number} is negative")
    elif number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is zero")

#A2
ages = [1, 10, 15, 25]
for age in ages:
    if age < 3:
        print("toddler")
    elif age < 13:
        print("child")
    elif age < 18:
        print("teenager")
    else:
        print("adult")

#A3
users = [
    {"username": "Bob", "password": "banana"}
    ]
user_input = input("Username: ")
user = next((user for user in users if user["username"] == user_input), None)

if (user):
    passw = input("password: ")
    if(passw == user["password"]):
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("username does not exist")

#A4
scores = [86, 25, 67, 83, 93]
for score in scores:
    if (score > 90):
        print("A")
    elif (score > 80):
        print("B")
    elif (score > 70):
        print("C")
    elif (score > 60):
        print("D")
    else:
        print("F")

#A5
members = ["Anna", "Bob"]
customers = [{"name": "Anna", "orders": 62},
             {"name": "Bob", "orders": 3},
             {"name": "Cecar", "orders": 81},
             {"name": "Dedric", "orders": 105}
             ]
for customer in customers:
    if (customer["name"] in members and customer["orders"] > 10 or customer["orders"] > 100):
        print("shipping is free")
    else:
        print("shipping fee not included")

#A6
print(False == False) #true
print(False == True) #false
print("one" != "0ne") #true
print(5 > 2) #true
print('a' > 'G') #true