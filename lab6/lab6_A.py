#A1
numbers = []
for i in range(1,21):
    numbers.append(i**2)
print(numbers)
numbers = [number ** 2 for number in range(1,21)]
print(numbers)

#A2
even_numbers = [number for number in range(1, 101) if number % 2 == 0]
print(even_numbers)

#A3
names = ["Ada", " bOb", " cecil  "]
names = [name.strip().title() for name in names]
print(names)

#A4
scores = [50, 67, 82, 90, 51]
passed_scores = [score for score in scores if score >= 70]
print(passed_scores)

#A5
graded_scores = dict({score: "PASS" for score in scores if score >= 70}|
                     {score: "FAIL" for score in scores if score < 70})

print(graded_scores)

#A6
#from lab3_A4
scores = [86, 25, 67, 83, 93]
'''
for score in scores:
    if (score > 90):
        print("A")
    elif (score > 80):
        print("B")
    elif (score > 70):
        print("C")
    elif (score > 60):
        print("D")
    else:
        print("F")
'''
graded_scores = dict({score: "A" for score in scores if score > 90}|
                     {score: "B" for score in scores if score <= 90 and score > 80}|
                     {score: "C" for score in scores if score <= 80 and score > 70}|
                     {score: "D" for score in scores if score <= 70 and score > 60}|
                     {score: "F" for score in scores if score <= 60})
print(graded_scores)

#from lab3_B2
languages = ["a", "b", "c"]
language_queries = ["c", "c++", "c#"]
#for lang in language_queries:
#    print (lang in languages)
result = [lang in languages for lang in language_queries]
print(result)

#from lab3_B4
blocked_usernames = ["John", "Peter"]
user_queries = ["Ada", "Berry", "Peter"]
#for name in user_queries:
#    if not name in blocked_usernames:
#        print (name)
result = [user for user in user_queries if user not in blocked_usernames]
print(result)