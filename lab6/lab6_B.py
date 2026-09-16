import unicodedata
#B1
d = {n: n ** 2 for n in range(1,11)}
print(d)

#B2
words = ["these", "are", "some", "words"]
d = {word: len(word) for word in words}
print(d)

#B3
names = ["Jakob", "José", "Jakob", "jakob", "jAkOb"]
normalized_lower_names_set = {unicodedata.normalize('NFD',name.lower()) for name in names}
print(normalized_lower_names_set)

#B4
products = {"Apple": 5, "Banana": 6, "Cucumber": 10}
cheap_products = {product: price for product, price in products.items() if price < 8}
print(cheap_products)

#B5
students = [{"name": "Ada", "score": 80},
            {"name": "Bob", "score": 60},
            {"name": "Cecil", "score": 70}]

student_grades = dict({student["name"]: "PASS" for student in students if student["score"] >= 70}|
                      {student["name"]: "FAIL" for student in students if student["score"] < 70})
print(student_grades)
