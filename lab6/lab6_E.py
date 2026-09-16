#E1
words = ["these", "are", "some", "words"]
sorted_by_length = sorted(words, key = lambda word: len(word))
print(sorted_by_length)

#E2
students = [{"name": "Ada", "score": 80},
            {"name": "Bob", "score": 60},
            {"name": "Cecil", "score": 70}]
students_by_score = sorted(students, key = lambda student: student["score"])
print(students_by_score)
students_by_score_decending = sorted(students, key = lambda student: student["score"], reverse = True)
print(students_by_score_decending)

#E3
products = [{"name": "Apple", "price": 6},
            {"name": "Banana", "price":  5},
            {"name": "Cucumber", "price": 10}]
sorted_products = sorted(products, key = lambda x: x["price"])
print(sorted_products)

#E4
people = [{"first_name": "Ada", "last_name": "Wong"},
          {"first_name": "Bob", "last_name": "Dylan"},
          {"first_name": "Cecil", "last_name": "Shorts"}]
sorted_people = sorted(people, key = lambda x: x["last_name"])
print(sorted_people)

#E5
def sort_key(item):
    return item["last_name"]

sorted_people = sorted(people, key = sort_key) #cleaner if the sort function already exists e.g. len(x)
print(sorted_people)
sorted_people = sorted(people, key = lambda x: x["last_name"]) #cleaner than having to write a new sort_key function