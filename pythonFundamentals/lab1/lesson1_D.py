#D1
s = "0123456789"
a = s[:] # "0123456789"
b = s[1:] # "123456789"
c = s[:1] # "0"
d = s[-1:] # "9"
e = s[:-1] # "012345678"
f = s[::5] # "05"
g = s[::-5] # "94"
h = s[2::-5] # "2"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

#D2
s = "ArtificialIntelligence"
a = s[:] #whole string
b = s[1:2] #substring from character 1 until (but not including) character 2
c = s[-1:1]  #sub starting 1 character from end until 1 character from begining (empty string)
d = s[-1:1:-1] #same as before but stepping backwards, this string is now entire string minus first and last character and backwards
e = s[1:-1] #entire string except first and last character
f = s[1:-1:-1] #empty string (since it's not stepping towards the end)

#D3
x = [1, 2, 3, 4]
x[0], x[1] = "one two".split()
x[2] = "  three   ".strip()
x[3] = "pour".replace("p", "f")
for i in range(4):
    print(x[i])

#D4
s = "something"
try:
    s[0] = "d"
except:
    print("something went wrong")
s = "d" + s[1:]
print(s)
