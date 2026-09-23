#C1
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

#C2, C3
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

#C4
account_1 = SavingsAccount("Ada", 50, 0.03)
account_2 = SavingsAccount("Bob", 100, 0.02)
print(account_1.owner, account_1.balance, account_1.interest_rate)
print(account_2.owner, account_2.balance, account_2.interest_rate)

#C5
#SavingsAccount is an Account but not all Accounts are SavingAccounts
