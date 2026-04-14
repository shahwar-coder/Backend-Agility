class User:
    def __init__(self, username, email, password):
        self.name = username
        self.email = email
        self.__password = password  # "Private" variable (name mangled)

    def check_password(self, password):
        return self.__password == password

u = User("shahwar", "shahwar@gmail.com", "secret123")

print(u.name)      
print(u.email)      
print(u.__password) # AttributeError: 'User' object has no attribute '__password'

'''
This example demonstrates **private variables using name mangling** in Python.

- __password → double underscore makes it "private-like"
- Python internally changes its name to:
  _User__password  (called name mangling)

Why error occurs:
👉 print(u.__password) raises AttributeError
   because __password is NOT stored with that exact name.

Actual internal name:
👉 u._User__password   ✅ (this works, but should NOT be used directly)

Method usage:
- check_password() safely compares input with stored password
- This is the correct way to access private data

Key Concept:
👉 Double underscore (__var) = prevents accidental access / override
   especially useful in inheritance

Best Practice:
👉 Never access __password directly
👉 Always use methods like:
   u.check_password("secret123")

Summary:
- _var   → protected (convention)
- __var  → private (name mangling)
'''