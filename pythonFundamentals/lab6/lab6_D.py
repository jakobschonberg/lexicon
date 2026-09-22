#D1 & D5
names = ["Ada", "Bob", "Cecil"]
scores = [66, 77, 88]
for name, score in zip(names, scores):
    print(name, score)

#D2
d = dict(zip(names, scores))
print(d)

#D3
product_names = ["Apple", "Banana", "Cucumber"]
prices = [5, 6, 10]
stock = [1, 2, 3]
combined_list = list(zip(product_names, prices, stock))
print(combined_list)

#D4
stock = [1]
combined_list = list(zip(product_names, prices, stock)) #zipped length is length of shortest list
print(combined_list) 

#D5
#see D1

#D6
a = 0
b = 1
print(a, b)
a, b = b, a
print(a, b)