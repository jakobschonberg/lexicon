from collections import defaultdict
#G1 #What happened to F?
def min_and_max(values):
    '''returns min_value, max_value from given list of values'''
    min = None
    max = None
    for value in values:
        if min == None or value < min:
            min = value
        if max == None or value > max:
            max = value
    return min, max

mini, maxi = min_and_max([0, 1, 2, 3, -1, 2])
print("Min:", mini)
print("Max:", maxi)

#G2
def is_palindrome(word):
    '''checks if word is a palindrom. returns True or False'''
    return word == (word[::-1])

print(is_palindrome("palindrome"))
print(is_palindrome("AYAYA"))

#G3
def character_count(s):
    '''counts characters in a string and returns a dictionary with the counts for each character'''
    r = defaultdict(int)
    for c in s:
        r[c] += 1        
    return r

print(character_count("coding python"))

#G4
numbers = [-5, 6, 4, 0, -2, 0, 5, 5]
def sign_count(numbers):
    '''counts positive, negative and zeros in a list of numbers'''
    r = defaultdict(int)
    for number in numbers:
        if(number < 0):
            r["negative"] += 1
        elif(number > 0):
            r["positive"] += 1
        else:
            r["zero"] += 1
    return r

print(sign_count(numbers))

#G5
def recursion():
    """Don't call this"""
    return recursion()
    