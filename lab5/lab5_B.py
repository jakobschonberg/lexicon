#B1
from functools import reduce
def add_all(*numbers):
    return reduce(lambda x, y: x + y, numbers)

print(add_all(1,2,3,4,5))

#B2
def average(*numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)

print(average(1,2,3,4,5))

#B3
def longest_word(*words):
    longest = None
    for word in words:
        if not longest or len(word) > len(longest):
            longest = word
    return longest

print(longest_word("longest", "word", "in", "this", "sentance", "is", "not", "this"))

#B4
def build_sentance(separator, *words):
    return separator.join(words)

print(build_sentance(" ", "This", "is", "a", "sentance"))

#B5
def describe_scores(student_name, *scores):
    return student_name, len(scores), average(*scores)

print(describe_scores("Ada", 1, 2, 3, 4, 5))