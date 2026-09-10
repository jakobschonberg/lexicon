#C1
names = ["Alva", "Bertil", "Cecil"]
for num, name in enumerate(names):
    print(f"{num}: Hello {name}")

#C2
s = "" 
for num in range(1, 51):
    if (num%2 == 0):
        if (s == ""):
            s += str(num)
        else:
            s += " " + str(num)
print(s) #one of many ways of printing the numbers on a line as to not take up too much vertical space

#C3
l = [6, 96, 39]
s = 0
for i in l:
    s += i
print(s)

#C4
m = None
for i in l:
    if m == None or i > m:
        m = i
print(m)

#C5
cnt = 0
for name in names:
    if(len(name) > 5):
        cnt += 1
print(cnt)

#C6
scores = [84, 68, 68, 39, 60, 49]
cnt_pass = 0
cnt_fail = 0
for score in scores:
    if score >= 70:
        cnt_pass += 1
    else:
        cnt_fail += 1
print(cnt_pass, cnt_fail)

#C7
my_dict = {0: 4,
     "thing": 11,
     "other thing": 42}
for key in my_dict:
    print(key, my_dict[key])
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)
