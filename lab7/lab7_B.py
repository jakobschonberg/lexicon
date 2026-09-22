#B1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

book2 = Book("The Silmarillion", "J.R.R. Tolkien", 443)
book3 = Book("2001 A Space Odyssey", "Arthur C. Clarke", 266)

print(book2.is_long(), book3.is_long())

#B2 and B3
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, change):
        self.balance += change

    def withdraw(self, change):
        if change > self.balance:
            raise ValueError("Ammount exceeds balance")
        self.balance -= change

bank_account = BankAccount("Ada")
bank_account.deposit(67)
print(bank_account.owner, bank_account.balance)
bank_account.withdraw(42)
print(bank_account.owner, bank_account.balance)
try:
    bank_account.withdraw(42)
except Exception as e:
    print(e)
print(bank_account.owner, bank_account.balance)

#B4
class Task:
    def __init__(self, title, completed = False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

#B5
task1 = Task("Complete labs")
task2 = Task("Wait")
print(task1.completed, task2.completed)
task1.complete()
print(task1.completed, task2.completed)

