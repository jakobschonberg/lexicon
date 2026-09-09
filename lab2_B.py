#B1
t = (127, 63, 0)
r, g, b = t
print(f"{r} {g} {b}")

#B2
t = ("Jakob", "48", "Täby")
name, age, city = t
print(f"{name} from {city} is {age} years old")

#B3
'''
Tuples are immutable, meaning you cannnot change their elements.
You can however change the whole Tuple.
A tuple is more lightweight than a list, so could be useful for performance reasons.
Also if you know something should be treated as a whole object and never partly changed,
 it could make sense to use a tuple to discourge mistakes.
'''

#B4
l = [(0, 0), (1, 2), (3, 4), (5, 6)]
print(l[1][0])
print(l[-1][-2])