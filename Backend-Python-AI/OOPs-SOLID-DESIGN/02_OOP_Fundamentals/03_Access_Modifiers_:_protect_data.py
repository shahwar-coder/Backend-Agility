class User:
    def __init__(self, username, email, password):
        self.name=username
        self.email=email
        self._password=password

# Protected Password


'''
This code defines a simple User class with basic attributes.

- name → public attribute (can be accessed directly)
- email → public attribute
- _password → protected attribute (by convention)

Key Concept:
👉 The single underscore (_) before password indicates it is "protected".

Meaning:
- It is NOT strictly private (Python does not enforce it).
- But it is a convention that this variable should NOT be accessed directly
  outside the class.

Example:
user = User("Shahwar", "abc@gmail.com", "1234")

user.name        ✅ allowed
user.email       ✅ allowed
user._password   ⚠️ allowed but NOT recommended

Why use protected?
👉 To signal developers:
   "This is internal data, don’t touch directly."

Best Practice:
👉 Access or modify password via methods (getters/setters or authentication logic),
   not by directly accessing _password.

Note:
- For stronger restriction, use __password (double underscore → name mangling).
'''