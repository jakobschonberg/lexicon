#F1
for i in range(1, 101):
    if (i%7 == 0 and i%9 == 0):
        print(i)
        break
    if(i%20 == 0):
        print("looping.... " + str(i)) #just to show that it actually stops after 63

#F2
s = ["", "string", "another string", "", "yet another string"]
for i in s:
    if(not i):
        continue
    print(i)

#F3
targets = ["strong", "strim", "string"]
for target in targets:
    found = next((x for x in s if x == target), None) #next breaks when first found, which I guess was the idea
    if (found):
        print("Found: ", target)
        break #just for good measure, not really required here but yeah...
    else:
        print("Not Found: ", target)

#F4
numbers = [-5, 6, 33.333, 67, 83, -50, 999, 63, 12]
for number in numbers:
    if number < 0:
        continue
    if number == 999:
        break
    print (number)
