from datetime import datetime
from datetime import timedelta

#H1, H2, H3
class User:
    def __init__(self, username, email, login_status = False):
        self.username = username
        self.email = email
        self.login_status = login_status

    def login(self):        
        self.login_status = True
        return "Welcome: " + self.username

    def logout(self):
        self.login_status = False
        return "Goodbye: " + self.username

#H4, H5, H6, H7, H9
class AdminUser(User):
    def __init__(self, username, email, login_status = False, root_access = False):
        super().__init__(username, email, login_status)
        self.root_access = root_access

    def goto_Root(self):
        if not self.root_access:
            raise PermissionError("No access to root")
        raise NotImplementedError("Root functionality not implemented")

    def login(self):
        welcome = super().login()
        return welcome[:7] + " admin user" + welcome[7:]

class PremiumUser(User):
    def __init__(self, username, email, premium_expiration_date, login_status=False):
        super().__init__(username, email, login_status)
        if (premium_expiration_date < datetime.now()):
            raise ValueError("Cannot create Premium user with already expired premium access")
        self.premium_expiration_date = premium_expiration_date

    def add_time_to_premium(self, time_delta):
        self.premium_expiration_date += time_delta

    def login(self):
        welcome = super().login()
        return welcome[:7] + " premium user" + welcome[7:]

#H8
user = User("Ada", "ada@mail.com")
admin = AdminUser("Bob", "bob@mail.com", False, True)
premium = PremiumUser("Cecil", "cecil@mail.com", datetime(2026, 11, 11, 12, 0))
print(user.login())
print(admin.login())
print(premium.login())
premium.add_time_to_premium(timedelta(days = 7))
print(premium.premium_expiration_date)
print(user.logout())
print(admin.logout())
print(premium.logout())

#H10
#an AdminUser is a User, a PremiumUser is a User, they both make use of the base class methods and attributes so we don't have to define those multiple times


