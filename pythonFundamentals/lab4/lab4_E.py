#E1
def degree_sign():
    return u'\N{DEGREE SIGN}'

def celsius_to_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

def classification(c):
    '''Temperature argument needs to be in celsius'''
    if (c < 0):
        return "cold"
    if (c >= 25):
        return "hot"
    return "warm"

#E2
basket = [{"Name": "Apple", "Price": 5, "Discount": 0.1},
          {"Name": "Banana", "Price": 9, "Discount": 0},
          {"Name": "Cucumber", "Price": 14, "Discount": 0}
          ]

def subtotal(items):
    return sum(x["Price"] for x in items)

def final_total(items):
    return sum(x["Price"]*(1-x["Discount"]) for x in items)

def total_discount(items):
    return subtotal(items) - final_total(items)

#E3
'''
name = "Jakob"
age = 48
height = 1.95
is_student = True
print (name)
print (type(name))
print (age)
print (type(age))
print (height)
print (type(height))
print (is_student)
print (type(is_student))
'''

l = ["Jakob", 48, 1.95, True]
def string_and_type(s):
    return str(s) + " | " + str(type(s))

def print_string_and_type(s):
    print(string_and_type(s))

def print_string_and_type_for_list(l):
    for item in l:
        print_string_and_type(item)

#E4
def main():
    print(f"{celsius_to_fahrenheit(37):.1f} {degree_sign()}F")
    print(f"{fahrenheit_to_celsius(100):.1f} {degree_sign()}C")
    print(subtotal(basket))
    print(final_total(basket))
    print(total_discount(basket))
    print_string_and_type_for_list(l)

main()
