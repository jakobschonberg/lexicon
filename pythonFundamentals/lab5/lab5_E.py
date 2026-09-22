#E1
def log_event(event_type, *messages, **metadata):
    e = dict(metadata)
    e["Messages"] = messages
    d = dict()
    d[event_type] = e
    return d

print(log_event("Click", "Hello", "World", time = "13:58", date = "2026-09-15"))

#E2
def calculate_order(customer, *prices, **options):
    print("Hello", customer)
    total = 0
    discount = 0
    shipping_fee = 0
    for key in options.keys():
        if(key == "discount"):
            discount = options["discount"]
        if(key == "shipping_fee"):
            shipping_fee = options["shipping_fee"]
    for price in prices:
        total += price * (1 - discount)
    total += shipping_fee
    return total

print(calculate_order("Ada", 1, 2, 3, 4, 5, discount = 0.1, shipping_fee = 10))

#E3 #kwargs version of E2
def calculate_order(customer, *prices, **kwargs): #less clear what we are supposed to put in kwargs
    print("Hello", customer)
    total = 0
    discount = 0
    shipping_fee = 0
    for key in kwargs.keys():
        if(key == "discount"):
            discount = kwargs["discount"] #hint of what might go in kwargs (but we have to read several lines to get here)
        if(key == "shipping_fee"):
            shipping_fee = kwargs["shipping_fee"] #another hint of what might go in kwargs
    for price in prices:
        total += price * (1 - discount)
    total += shipping_fee
    return total

#E4
def average(*numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)

print(average())
print(average(0))
print(average(1, 2, 3, 4, 5))