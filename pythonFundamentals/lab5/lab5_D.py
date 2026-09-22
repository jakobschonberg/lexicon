#D1
def show_profile(**info):
    for key, value in info.items():
        print(key, value)

profile = {"Name": "Ada", "Age": 22, "IsStudent": True}
show_profile(**profile)

#D2
def create_user(username, **details):
    d = dict()
    d[username] = details
    return d

d = create_user("Jakob", Age = 48, City = "Täby")
print(d)

#D3
def build_product(name, price, **metadata):
    e = dict(metadata)
    e["Price"] = price
    d = dict()
    d[name] = e
    return d

d = build_product("Apple", 10, Weight = 0.3, Color = "red")
print(d)

#D4
def get_set_settings(**settings):
    d = dict()
    for key, value in settings.items():
        if value != None:
            d[key] = value
    return d

print(get_set_settings(Ready = True, Compiled = False, Verified = None))

#D5
def greet(first_name, last_name, city):
    print("Hello", first_name, last_name, "from", city)

d = {"first_name": "Jakob", "last_name": "Schönberg", "city": "Täby"}
greet(**d)
