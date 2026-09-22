#C1
l = [10, 20, 30]
def fun(a, b, c):
    return a + b + c
print(fun(*l))

#C2
person = ("Jakob", "Schönberg", "Täby")
def greet(first_name, last_name, city):
    print("Hello", first_name, last_name, "from", city)
greet(*person)

#C3
def fun(first, *middle, last = "default_value"):
    return f"{first} | {middle} | {last}"
print(fun("Hi", "Mid0", "Mid1"))
print(fun("Hi", "Mid0", "Mid1", "Mid2"))
print(fun("Hi", "Mid0", "Mid1", last = "Last"))
print(fun(("First0", "First1"), "Mid0", "Mid1", last = ("Last0", "Last1")))

#C4
def fun(*args): #*args means args is a tuple of any length
    print(args) #prints the tuple
    print(*args) #prints the unpacked tuple

fun(1,2,3)