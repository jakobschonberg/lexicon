#G1
users0 = ["a", "c"]
users1 = ["a", "b"]
dup = set(users0) & set(users1)
print(dup)
uniq = set(users0) ^ set(users1)
print(uniq)

#G2
platform = [{"name": "python",
             "teacher": "Alladin",
             "students": ["Jakob", "Marcus", "Christian", "Jacob"],
             "topics": ["fundamentals", "advanced"]},
             {"name": "AI",
              "teacher": "Haithem",
              "students": ["Jakob", "Marcus", "Christian", "Jacob"],
              "topics": ["queries", "LLMs"]}]

#G3
inv = {"cola": 0, "fanta": 0, "pepsi": 0, "sprite": 0, "7up": 0}
inv["cola"] = 5
inv["fanta"] = 6
inv["pepsi"] = 7
inv["sprite"] = 8
inv["7up"] = 1

#G4
'''
list: best when you want to access by a specific index, change specific index s[32] += 2
tuple: best when you want the entire object to be considered 1 item, so you can't change
 a part of it, better performance than list
 set: best when you want to enforce that no duplicate items are in the collection
 dictionary: best when you want a key-value relationship and ability to "look up" or change
  values based on keys or get key-value pairs (keys are unique)
'''




