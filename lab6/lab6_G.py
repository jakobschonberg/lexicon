#G1
list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
my_list = [item for list_item in list_of_lists for item in list_item]
print(my_list)

#G2
mult_table = [[x * y for y in range(1, 11)] for x in range(1, 11)] #looks readible to me
print("mult table:")
for row in mult_table:
    s = ""
    for value in row:
        s = s + str(value).rjust(3)
    print(s)

#G3
students = [{"name": "Ada", "score": 80},
            {"name": "Bob", "score": 60},
            {"name": "Cecil", "score": 70}]
passed_students = [{"name": student["name"],
                    "score": student["score"]}
                    for student in students
                    if student["score"] >= 70]
print(passed_students)

#G4
any_students = False
for student in students:
    if student["score"] > 67:
        any_students = True
print(any_students)

any_students = any(student["score"] > 67 for student in students)
print(any_students)

all_astudents = True
for student in students:
    if student["score"] <= 67:
        all_astudents = False
print(all_astudents)

all_astudents = all(student["score"] > 67 for student in students)
print(all_astudents)

#G5
a = [1, 2, 3]
b = [4, 5, 6]
a_and_b = [*a, *b]
print(a_and_b)
a_zip_b = list(zip(a,b))
print(a_zip_b)
import numpy as np
a_cross_product_b = np.cross(np.array(a), np.array(b))
print("cross:", a_cross_product_b)
a_dot_b = sum(i[0] * i[1] for i in zip(a, b))
print("dot",a_dot_b)
squares = {number: number ** 2 for number in a}
print(squares)
