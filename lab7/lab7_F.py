#F1, F2, F3, F4, F5, F6, F7, F8
class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, score):
        if (score < 0):
            raise ValueError("score can not be negative")
        self.name = name
        self.score = score

    def get_status(self):
        if self.score >= 70:
            return "PASS"
        return "FAIL"

class Course:
    def __init__(self, name, teacher, students = []):
        self.name = name
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def count_students(self):
        return len(self.students)

    def passed_students(self):
        return [student for student in self.students if student.get_status() == "PASS"]

#F9
students = [
    Student("Ada", 66),
    Student("Bob", 77),
    Student("Cecil", 88),
    Student("Dave", 99),
    Student("Eve", 55)
]
teacher = Teacher("Frank")
course = Course("Python", teacher, students)
print(course.name, course.teacher.name, [student.name for student in course.students])

#F10
print(course.name)
print(teacher.name)
for student in course.passed_students():
    print(student.name)