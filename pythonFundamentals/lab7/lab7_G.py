#G1
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

    def update_score(self, new_score):
        if (new_score < 0):
            raise ValueError("score can not be negative")
        self.score = new_score

#G2
class Course:
#G4
    dependancies = [Student, Teacher]
    #class variable for keeping track of which classes this class depends on
    #should be a class variable since its value should be the same for all objects of the class

    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def count_students(self):
        return len(self.students)

    def passed_students(self):
        return [student for student in self.students if student.get_status() == "PASS"]

    def students_with_at_least_score_of(self, score_threshold):
        return [student for student in self.students if student.score >= score_threshold]

    def get_student_names(self):
        return [student.name for student in self.students]


#G3
students = [
    Student("Ada", 66),
    Student("Bob", 77),
    Student("Cecil", 88),
    Student("Dave", 99),
    Student("Eve", 55)
]
students2 = [
    Student("Ada", 66),
    Student("Bob", 77),
    Student("Cecil", 88),
    Student("Dave", 99),
    Student("Eve", 55)
]
teacher = Teacher("Frank")
teacher2 = Teacher("Frank")
course = Course("Python", teacher, students)
course2 = Course("AI", teacher2, students2)
print(course.students is course2.students)
course2.add_student(Student("Hans", 67))
print("students in course2 but not in course")
print([student.name for student in course2.students if student not in course.students])
print("student names in course2 but not in course:")
print([student.name for student in course2.students if student.name not in course.get_student_names()])
print("students in course:")
print([student.name for student in course.students])
print("students in course2:")
print([student.name for student in course2.students])


