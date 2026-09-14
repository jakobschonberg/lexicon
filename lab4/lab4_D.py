#D1
def calculate_total(numbers):
    r = 0
    for i in numbers:
        r += i
    return r

#D2
def count_even(numbers):
    r = 0
    for i in numbers:
        if (i % 2 == 0):
            r += 1
    return r

#D3
def get_long_words(words, minimum_length):
    r = []
    for word in words:
        if(len(word) >= minimum_length):
            r.append(word)
    return r

#D4
def find_student(students, name):
    for student in students:
        if student["Name"] == name:
            return student
    return None

students = [{"Name": "Ada", "Score": 30, "Active": True},
            {"Name": "Bob", "Score": 40, "Active": True},
            {"Name": "Cecil", "Score": 55, "Active": False}]
print(find_student(students, "Bob"))

#D5
def average_score(students):
    total = 0
    for student in students:
        total += student["Score"]
    return total / len(students)

print(average_score(students))

#D6
def get_active_users(users):
    r = []
    for user in users:
        if user["Active"]:
            r.append(user)
    return r

print(get_active_users(students))