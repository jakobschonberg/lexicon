#G1
def merge_settings(defaults, **overrides):
    d = dict()
    for key, value in defaults.items():
        d[key] = value
    for key, value in overrides.items():
        d[key] = value        
    return d

settings0 = {"bold": True, "italic": False, "size": 10}
settings1 = {"family": "comic sans", "italic": True}

print("merged: ", merge_settings(settings0, **settings1))
print("defaults: ", settings0)
print("overrides: ", settings1)

#G2
def fix_string(s):
    if not s.count("'"):
        return "'" + s + "'"
    if not s.count('"'):
        return '"' + s + '"'
    #both 's and "s in the string
    #return "'''" + s + "'''" would work if string doesn't start/end with a combination of ' and "
    r = ""
    if s[0] == "'":
        r = '"' + "'" + '"'
    splits = s.split("'")
    for split in splits:
        if (split):
            if r == "":
                r = "'" + split + "'"
            elif r == '"' + "'" + '"':
                r = r + " + '" + split + "'"
            else:
                r = r + ' + "' + "'" + '" + ' + "'" + split + "'"
    if s[-1] == "'":
        r = r + " + " '"' + "'" + '"'
    return r
    

def call_summary(function_name, *args, **kwargs):
    s = function_name + "("
    first_arg = True
    for arg in args:
        if not first_arg:
            s += ", "
        s += str(arg)
        first_arg = False
    for key, value in kwargs.items():
        if not first_arg:
            s += ", "
        s += str(key) + " = "
        if isinstance(value, str):
            s += fix_string(str(value))
        else:
            s += str(value)
    s = s + ")"
    return s  


print(call_summary("foobar", 1, 2, 3, **settings1))

def foobar(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

foobar(1, 2, 3, family = 'comic sans', italic = True)

#examples related to fixing strings with both ' and " in them
#we could have fixed this with """ or ''' but then we'd have to handle
#cases where string has actual ' start and " end or vice versa.
#all in all I think we have dived deep enough into guarding against weird strings for now
cooked_string = '"' + "That's one cooked string" + '"'
cooked_string2 = "'" + "That's another " + '"cooked"' + " string" + "'"
print(cooked_string)
print(fix_string(cooked_string))
print('"That' + "'" + 's one cooked string"')
print('''"That's one cooked string"''')
print(cooked_string2)
print(fix_string(cooked_string2))
print("'" + 'That' + "'" + 's another "cooked" string' + "'")
print("""'That's another "cooked" string'""")

#G3
def len(*numbers):
    r = 0
    for number in numbers:
        r += 1
    return r

def sum(*numbers):
    r = float(0)
    for number in numbers:
        r += float(number)
    return r

def average(*numbers):
    if not numbers:
        return 0
    return sum(*numbers)/len(*numbers)

def min(*numbers):    
    r = None
    for number in numbers:
        if r == None or number < r:
            r = int(number)
    return int(r)

def max(*numbers):
    r = None
    for number in numbers:
        if r == None or number > r:
            r = number
    return int(r)

def stats(*numbers):
    r = len(*numbers), sum(*numbers), average(*numbers), min(*numbers), max(*numbers)
    return r                

args = (1, 2, 3, 4, 5)
print(stats(*args))

#G4
a = 0
b = 0
c = 0
def fun():
    a = 1
    def fun_inner():
        def fun_inner_inner():
            c = 3
            print("inner_inner", a, b, c)
        b = 2
        fun_inner_inner()
        def fun_inner_inner2():
            c = 4
            print("inner_inner2", a, b, c)
        fun_inner_inner2()
        print("inner",a,b,c)
    fun_inner()
    print("fun",a,b,c)
fun()
print("global",a,b,c)