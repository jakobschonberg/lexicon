#D1, D2, D4
class Student:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "PASS"
        return "FAIL"

students = [
    Student("Ada", 55),
    Student("Bob", 66),
    Student("Cecil", 77),
    Student("Dave", 88),
    Student("Eva", 99),
    Student("Franz", 44)
]

#D3
for student in students:
    print(student.name, student.score)

#D5
for student in students:
    print(student.name, student.get_status())

#D6
passed_students = [student for student in students if student.score >= 70]
for student in passed_students:
    print("Passed: ", student.name)


