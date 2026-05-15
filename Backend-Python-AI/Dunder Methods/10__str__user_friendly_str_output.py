'''
TASK 1: USER-FRIENDLY STRING OUTPUT

Write a class `User` with:
- Attributes: id and name
- A __str__ method that returns a friendly message like:
  "User 1: Rahul"

TEST CASE:
- When print(user_object) is called,
  it should show the friendly message.

RULES:
- Implement __str__

GOAL:
Understand that __str__ defines how an object
is displayed to end users when printed.
'''

class User:
    "User Details"
    def __init__(self, user_id: str, name: str)->None:
        self.user_id = user_id
        self.name = name

    def __repr__(self)->str: # More Developer focused representation
        return f"User(user_id={self.user_id}, name={self.name})"
    
    def __str__(self)->str: # More Human-readable / User-Friendly representation
        return f"User {self.user_id} : {self.name}"
    

user1 = User("A123", "Rahul")
user2 = User("B123", "Priyanka")

print(user1)
print(user2)

# User A123 : Rahul
# User B123 : Priyanka

# By default, Python will opt for __str__ over __repr__.
# If __str__ is not there, it will default to __repr__.


'''
# Key Points (What This Implementation Demonstrates)
- Defines a User class with id and name attributes.
- Implements __str__ to produce a friendly, human-readable message.
- print(user) automatically calls the __str__ method.
- Output is designed for end users, not developers.

# Key Points (__str__ vs __repr__)
- __str__ → user-friendly, readable output.
- __repr__ → developer-focused, debugging representation.
- When both exist:
    print(object) → uses __str__
- If __str__ is missing:
    Python falls back to __repr__.

# Key Points (Behavior)
- print(user1) → "User A123 : Rahul"
- print(user2) → "User B123 : Priyanka"
- Each object displays its own data clearly.

# Backend / Design Perspective
- __str__ is useful for:
  - logs shown to users
  - CLI tools
  - status messages
- __repr__ is used for:
  - debugging
  - containers (lists, dicts)
  - developer inspection

# Core Takeaway
- __str__ controls the human-facing representation.
- __repr__ controls the developer-facing representation.
- Python prefers __str__ when printing an object.
'''
