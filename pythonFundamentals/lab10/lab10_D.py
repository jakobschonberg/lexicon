#D1
class User:
    pass

class AdminUser(User):
    pass

#D2
admin = AdminUser()

#D3, D4
print(isinstance(admin, AdminUser))
print(isinstance(admin, User))
print(isinstance(admin, str))

#D5
#AdminUser inherits from User and is therefor a User as well