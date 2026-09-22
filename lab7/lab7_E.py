#F1
class Teacher:
    def __init__(self, name):
        self.name = name

#F2, F3, F5, F6
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name, teacher, students = []):
        self.name = name
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        self.students.append(student)

teacher = Teacher("Aladdin")
course = Course("Python", teacher)
course.add_student(Student("Ada"))
course.add_student(Student("Bob"))
course.add_student(Student("Cecil"))

#F4
print(course.name, course.teacher.name)

#F7
for student in course.students:
    print(student.name)
