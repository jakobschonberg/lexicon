#H1, H2, H5
class Exporter:
    def export(self, data):
        return "exporting: " + str(data)
    def __str__(self):
        return "Exporter"

#H3, H4
class ConsoleExporter(Exporter):
    def export(self, data):
        return "console exporting: " + str(data)
    def __str__(self):
        return "ConsoleExporter"

class TextExporter(Exporter):
    def export(self, data):
        return "text exporting: " + str(data)
    def __str__(self):
        return "TextExporter"    

class SummaryExpoerter(Exporter):
    def export(self, data):
        return "summary exporting: " + str(data)
    def __str__(self):
        return "SummaryExpoerter"    

#H6
exporters = [
    Exporter(),
    ConsoleExporter(),
    TextExporter(),
    SummaryExpoerter()
]

#H7
for exporter in exporters:
    print(exporter.export(5))

#H8
class Student:
    def __init__(self, name):
        self.name = name
    def export(self, data):
        return f"Exporting by hand ({self.name}): " + str(data)
print(Student("Ada").export(7))

#H9
print(isinstance(TextExporter(), Exporter))
print(isinstance(Exporter(), TextExporter))
print(isinstance(Student("Bob"), Exporter))

#H10
class StudentClass:
    def __init__(self, students):
        if students is None:
            self.students = []
        else:
            self.students = students

students = [
    Student("Ada"),
    Student("Bob")
]
studentClass = StudentClass(students)
#The StudentClass has a number of students in it, it would not make sense to have it inherit from Student
#A "HAS-A" relationship makes much more sense.