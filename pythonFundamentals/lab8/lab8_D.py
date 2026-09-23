#D1
class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return "information"

#D2
class Developer(Employee):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def get_team(self):
        return self.team

#D3
class SalesPerson(Employee):
    def __init__(self, name, sales):
        super().__init__(name)
        self.sales = sales

    def add_sale(self):
        self.sales += 1

#D4
dev = Developer("Ada", "UI")
sales = SalesPerson("Bob", 0)
print(dev.get_information())
print(sales.get_information())

#D5
emp = Employee("Cecil")
try:
    print(emp.get_team())
except Exception as e:
    print(e)

