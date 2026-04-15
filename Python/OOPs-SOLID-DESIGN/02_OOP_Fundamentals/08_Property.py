class User:
    def __init__(self, username, email, password ) -> None:
        self.username=username
        self._email=email
        self.password=password

    # @property
    def email(self):
        return self._email

user = User("Rahul", "rahul001@gmail.com", "password@123")
# print(user.email) # (WHEN NO PROPERTY DEFINED and no METHOD) AttributeError: 'User' object has no attribute 'email' 
# print(user.email) # (WHEN NO PROPERTY DEFINED but METHOD is there) <bound method User.email of <__main__.User object at 0x104afae40>>
print(user.email) # (WHEN PROPERTY DEFINED) rahul001@gmail.com


'''
This example demonstrates the difference between:
👉 normal method vs @property in Python

-------------------------------------------------------

🔹 Case 1: No method, no @property
- Only _email exists (protected variable)
- Trying user.email ❌ → AttributeError
👉 Because attribute "email" is not defined

-------------------------------------------------------

🔹 Case 2: Method without @property
def email(self):
    return self._email

- Accessing user.email returns:
  <bound method User.email ...>

👉 Because:
- email is treated as a METHOD
- You must call it:
  user.email()  ✅

-------------------------------------------------------

🔹 Case 3: Using @property
@property
def email(self):
    return self._email

- Now user.email works like an attribute:
  user.email  ✅ → "rahul001@gmail.com"

👉 Because:
- @property converts method → attribute-like access

-------------------------------------------------------

🔑 Key Concept:
- method        → needs ()
- @property     → behaves like variable (no ())

-------------------------------------------------------

🔥 Why use @property?
- Cleaner syntax (no parentheses)
- Allows control over access
- Useful for validation / computed values

-------------------------------------------------------

✅ Best Practice:
Use @property when:
- You want read-only access
- You want to hide internal variables (_email)
- You may add logic later without changing interface
'''