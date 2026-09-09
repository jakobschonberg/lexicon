#C1
l = ["python", "python", "python", "c++", "c++"]
l2 = set(l)
print(len(l))
print(len(l2))

#C2
sk0 = {"c", "c++", "c#"}
sk1 = {"c++", "python"}
shared_skills = sk0 & sk1
print(shared_skills)
skills_first = sk0 - sk1
print(skills_first)
skills_any = sk0 | sk1
print(skills_any)

#C3
sk0.add("java")
sk0.remove("c")
sk0.discard("c++")
sk0.discard("c")
print(sk0)

#C4
'''
lets say you have travel path and you want to print a list of all visited cities
you are not intrested in duplicates, so you only want to store any city once
you could accomplish this with a list by always checking if the city is in the list before
inserting it, but it's much easier with a set since it automaticly prevents you from
inserting duplicate values.
'''