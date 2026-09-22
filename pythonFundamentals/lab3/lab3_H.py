#H1
for FizzBuzz in range(1, 101):
    s = ""
    if(FizzBuzz%3 == 0):
        s += "Fizz"
    if(FizzBuzz%5 == 0):
        s += "Buzz"
    if(s == "FizzBuzz"):        
        print(FizzBuzz, s)

#H2
vowels = ["a", "e", "i", "o", "u"]
sentance = "This is a sentance"
cnt = 0
for char in sentance:
    if char in vowels:
        cnt += 1
print(cnt)

#H3
lst = ["a", "b", "c", "b", "a", "d", "f", ""]
found = set()
duplicates = set()
for item in lst:
    if (item in found):
        duplicates.add(item)
    else:
        found.add(item)
print(duplicates)

#H4
lst = [3, 5, 2]
for i in lst:
    print("x" * i)
