# Protected
# Single underscore
# Can be directly accessed, but 'should' not be ethically
class User:
    def __init__(self, username, email, password):
        self.name = username
        self.email = email
        self._password = password  # Protected (by convention)


# Private
# Double Underscore
# Name is mangled so it cannot be accessed directly
class User:
    def __init__(self, username, email, password):
        self.name = username
        self.email = email
        self.__password = password  # Private (name mangled)

'''
This snippet compares **Protected vs Private variables in Python**.

🔹 Protected (_password)
- Uses single underscore: _password
- Can be accessed directly: user._password ✅
- But by convention, it "should not" be accessed outside the class
- It is only a soft restriction (no enforcement)

👉 Purpose:
Signal to developers → "internal use, avoid direct access"

-------------------------------------------------------

🔹 Private (__password)
- Uses double underscore: __password
- Cannot be accessed directly: user.__password ❌
- Python internally renames it to: _ClassName__password
  (called name mangling)

👉 Example:
user._User__password  ✅ (works, but not recommended)

👉 Purpose:
- Avoid accidental access
- Prevent conflicts in inheritance

-------------------------------------------------------

🔑 Key Difference:
- _var   → convention-based protection (weak)
- __var  → name mangling (stronger protection)

-------------------------------------------------------

✅ Best Practice:
Always access sensitive data (like password) via methods
instead of direct attribute access.
'''