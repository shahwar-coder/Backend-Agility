'''
Protected 
- `_`
- one underscore
- can be accessed outside class but not recommended

Private
- `__`
- double underscore
- cannot be accessed outside class
'''

class User:

    # Protected method
    def _show_info(self):
        print("This is a protected method")

    # Private method
    def __show_secret(self):
        print("This is a private method")

    def access_methods(self):
        # Accessing both inside class 
        self._show_info()
        self.__show_secret()


u = User()

# Works (but not recommended)
u._show_info()

# Fails (private)
# u.__show_secret()   # AttributeError

# Works internally
u.access_methods()




'''
This example explains **Protected vs Private methods in Python**.

=======================================================

🔹 Protected Method: _show_info()

- Defined using single underscore: _
- Can be accessed outside the class
  u._show_info()  ✅ (works)
- But "should not" be accessed directly (convention)

👉 Purpose:
- Indicates internal use
- Soft restriction (developer discipline)

-------------------------------------------------------

🔹 Private Method: __show_secret()

- Defined using double underscore: __
- Cannot be accessed directly:
  u.__show_secret() ❌ → AttributeError

👉 Why?
- Python uses **name mangling**
- Internally renamed to:
  _User__show_secret

👉 Technically accessible:
u._User__show_secret()  ✅ (but NOT recommended)

-------------------------------------------------------

🔹 Access inside class:

def access_methods(self):
    self._show_info()       ✅
    self.__show_secret()    ✅

👉 Both methods are fully accessible within the class

-------------------------------------------------------

🔑 Key Difference:

Protected (_method):
- Accessible outside (but discouraged)
- Convention-based restriction

Private (__method):
- Not directly accessible
- Name mangling applied
- Stronger protection

-------------------------------------------------------

⚠️ Important Note:
👉 Python does NOT enforce true privacy
👉 It uses conventions + name mangling

-------------------------------------------------------

🔥 Real-world analogy:

Protected:
👉 "You *can* access it, but please don’t"

Private:
👉 "You’re not supposed to access this at all"

-------------------------------------------------------

✅ Best Practice:

- Use _method → for internal/helper methods
- Use __method → for sensitive/internal logic
- Always access through public methods when possible

-------------------------------------------------------

🎯 Interview One-liner:

👉 "_protected is a convention, __private uses name mangling for stronger access control."
'''