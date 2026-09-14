#B1
def is_even(number):
    return number % 2 == 0

#B2
def get_larger(a,b):
    if(a > b):
        return a
    return b

#B3
def classify_score(score):
    if(score >= 70):
        return "PASS"
    return "FAIL"

#B4
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

#B5
def calculate_discount(price, percent):
    '''Returns the adjusted price.
    percent parameter expects a fraction value'''
    return price * (1 - percent)

#B6
def print_stuff(stuff):
    print(stuff)

a = print_stuff(5)
print(a)