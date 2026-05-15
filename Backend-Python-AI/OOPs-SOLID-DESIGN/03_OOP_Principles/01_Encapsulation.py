'''
Encapsulation is about hiding data and providing controlled access.

1. Data Hiding : 
- internal data is protected using `_` and `__`.
- these are protected and private respectively.

2. Controlled Access : 
- access/modification via methods or @property(getters/setters).
- allows adding validations/business logic.

3. Better Design :
- internal implementation can change without affecting external code.
- reduces bugs, improves maintainability.
'''


'''
Encapsulation = hiding data + controlled access
'''

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password   # Data Hiding (private)

    # Controlled Access (getter)
    @property
    def password(self):
        return "*****"   # hide actual password

    # Controlled Access (setter with validation)
    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            print("Password too short")
        else:
            self.__password = new_password
            print("Password updated")

    # Method using internal data
    def check_password(self, pwd):
        return self.__password == pwd


# Usage
u = User("Shahwar", "secret123")

print(u.password)        # ***** (hidden)

u.password = "123"       # alidation
u.password = "newpass"   # update

print(u.check_password("newpass"))  # True


'''
What this shows:

1. Data Hiding:
   __password is private

2. Controlled Access:
   getter + setter control access and validation

3. Better Design:
   we can later hash password internally without changing usage
'''