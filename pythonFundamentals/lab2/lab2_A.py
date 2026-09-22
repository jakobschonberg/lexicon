#A1
l = ["c", "c++", "c#", "python", "java", "basic", "assembler", "whitespace"]
print(l[0])
print(l[2])
print(l[-1])

#A2
print(l[0:1])
print(l[1:3])
print(l[6:])
print(l[::-1])

#A3
l.append("brainf***")
print(l)
l.insert(3, "perl")
print(l)
l.remove("java")
print(l)
l.pop(0)
print(l)

#A4
numbers = [5, 6, 7]
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#A5
l.sort()
lc = sorted(l, reverse = True)
#lc = l.copy()
#lc.sort(reverse = True)
print(l)
print(lc)
#sorted() doesn't change the original list, sort() changes the original list

#6
list_a = [6]
list_b = list_a
list_b.append(7) #changes both list_a and list_b since they are referencing the same memory
print(list_a)
list_a = [6]
list_b = list_a.copy() #creates a new list that is a seperate copy
list_b.append(7)
print(list_a)