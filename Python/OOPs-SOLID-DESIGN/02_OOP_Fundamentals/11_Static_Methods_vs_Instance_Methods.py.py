'''
Static methods are the methods that belong to class itself, 
and not to any instance of the class.

To define  static method we use the `@staticmethod` decorator.
'''


class User:
    def __init__(self, name):
        self.name = name   # instance variable

    # Instance Method
    def greet(self):
        print(f"Hello, I am {self.name}")  # uses instance data

    # Static Method
    @staticmethod
    def say_hello():
        print("Hello! Welcome to the system")  # no instance data used


# Create object
u = User("Shahwar")

# Calling instance method (needs object)
u.greet()         # Hello, I am Shahwar

# Calling static method
u.say_hello()     # Hello! Welcome to the system
User.say_hello()  # also works



'''
This example explains **Instance Method vs Static Method** clearly.

=======================================================

🔹 Instance Method:
def greet(self):

- Requires an object (instance) to be called
- Has access to instance variables via self
- Works with object-specific data

👉 Example:
u.greet()
→ uses self.name ("Shahwar")

-------------------------------------------------------

🔹 Static Method:
@staticmethod
def say_hello():

- Does NOT require an object
- Does NOT use self or cls
- Cannot access instance or class variables directly
- Behaves like a normal function, but logically grouped inside the class

👉 Can be called in 2 ways:
User.say_hello()   ✅ (preferred)
u.say_hello()      ✅ (also works)

-------------------------------------------------------

🔍 Key Difference:

Instance Method:
- Needs object
- Uses instance data (self)

Static Method:
- No object needed
- No access to instance/class data
- Utility/helper function related to class

-------------------------------------------------------

🧠 When to use Static Method?

👉 When:
- Logic is related to class conceptually
- But does NOT depend on instance data

Examples:
- Validation functions
- Utility helpers
- Formatting logic

-------------------------------------------------------

🔥 Real-world analogy:

Instance Method:
👉 Like a person speaking about themselves
"I am Shahwar"

Static Method:
👉 Like a general announcement
"Welcome to the system"

-------------------------------------------------------

🔑 Summary:

- self      → instance method
- no self   → static method
- uses data → instance method
- utility   → static method

-------------------------------------------------------

🎯 Interview One-liner:

👉 "Static methods don’t access instance or class state; they are utility functions logically grouped inside a class."
'''