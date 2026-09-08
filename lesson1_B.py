#B1
import datetime
name = input("Name: ")
birth_year = int(input("Year of birth: "))
print ("Approximate age: " + str(datetime.datetime.now().year - birth_year))

#B2
price = float(input("Price: "))
discount = float(input("Discount %: "))
print("Discounted price: " + str(round(price * (1 - discount / 100), 2)))

#B3
degree_sign = u'\N{DEGREE SIGN}'
temp = float(input("Temperature in " + degree_sign + "C: "))
print (str(round(temp * 9 / 5 + 32, 1)) + " " + degree_sign + "F")

#B4
length = float(input("Length: "))
width = float(input("Width: "))
area = length * width
perimeter = 2 * (length + width)
print ("Area: " + str(area))
print ("Perimeter: " + str(perimeter))

#B5
#doing something like int("hello") should give a ValueError
# so if user enters a string where an int or float is expected
# the program will terminate with the error
# (since we are not handling the exception)
