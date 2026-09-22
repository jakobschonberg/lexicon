#A1

course_name = "Python"

def greet():
    print("Hello World!")

def show_coursename():
    print(course_name)

def print_separator():
    print("---")

greet()
print_separator()
show_coursename()
print_separator()
greet()
print_separator()
show_coursename()

#A2
def greet_person(name):
    print("Hello", name)

def introduce(name, city):
    print (name, "from", city)

#A3, A4
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): #parameters a and b
    return a / b

print(divide(18, 3)) #arguments 18 and 3

#A5
def calculate_area(width, height):
    return width * height

depth = 6
volume = depth * calculate_area(5, 4)

print(volume)

