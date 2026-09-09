#D1
laptop = {"brand": "acer",
          "model": "T-180",
          "RAM": "16 Gb",
          "storage": "1 Tb",
          "price": 900}
print(laptop["brand"])
print(laptop["model"])
print(laptop["RAM"])
print(laptop["storage"])
print(laptop["price"])

#D2
laptop["price"] = 950
laptop["operating_system"] = "windows 11"
laptop.pop("model")
print(laptop)

#D3
print(laptop.get("brand"))
print(laptop.get("model"))
'''
unless it's an ordered dictionary, dictionaries don't guarantee order,
 so getting by index is not an option (for this dictionary)
 further unless the dictionary is indexed, it will take at least O(log N) time to find an
 item in a dictionary, where as getting by index will find it in O(1) time.
 Indexing however increases storage costs, insertion time etc...
'''

#D4
print(*laptop.keys())
print(*laptop.values())
print(*laptop.items())

#D5
course_hours = {
    "python": 11,
    "algebra": 7,
    "calculus": 12,
    "ai": 0,
    "quantum physics": 5}
total = sum(course_hours.values())
print(total)
          
