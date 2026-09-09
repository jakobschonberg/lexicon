#E1
l = [
    {"title" : "A",
     "author" : "a",
     "pages" : 4,
     "available" : True},
     {"title" : "B",
      "author" : "b",
     "pages" : 11,
     "available" : True},
     {"title" : "C",
     "author" : "c",
     "pages" : 190,
     "available" : False},
     {"title" : "D",
     "author" : "d",
     "pages" : 830,
     "available" : False},
     {"title" : "E",
     "author" : "e",
     "pages" : 1,
     "available" : True}
]

#E2
print(l[2]["title"])
print(l[-1]["available"])

#E3
l[-1]["available"] = False
l[-1]["destroyed"] = True

#E4
d = {"Board" : ["Jim", "Luke"],
     "Sales" : ["Anna"],
     "IT": ["Jakob", "Claude"]}
print(d)

#E5
courses = [
    {"name" : "Python",
     "teacher" : "Alladin",
     "topics" : ["Fundamentals", "algorithms"]},
     {"name" : "AI",
     "teacher" : "Haithem",
     "topics" : ["queries", "LLMs"]},
     {"name" : "SQL",
     "teacher" : "Haithem",
     "topics" : ["Basics", "Databases"]}
]
print(courses[0]["topics"][1])
