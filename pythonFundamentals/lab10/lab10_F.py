#F1, F2
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"{self.owner} - {self.balance}"

#F3, F4
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def __str__(self):
        return super().__str__() + f" - {self.interest_rate}"

#F5
account1 = Account("Ada", 10)
account2 = SavingsAccount("Bob", 24, 0.02)
print(account1)
print(account2)
    
