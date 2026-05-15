'''
TASK 1: READABLE OBJECT REPRESENTATION

Write a class `User` with:
- Attributes: id and name
- A __repr__ method that returns a clear string representation

EXPECTED BEHAVIOR:
- Printing the object should show meaningful information
- Printing a list of User objects should also show readable output

RULES:
- Implement __repr__ only (no __str__)
- The return value of __repr__ must be a string

GOAL:
Understand that __repr__ defines how objects appear
during debugging and in containers.
'''


class User:
    "A user system"
    def __init__(self, user_id: int, name: str)->None:
        self.user_id = user_id
        self.name = name

    def __repr__(self)->str:
        return f"User(user_id={self.user_id}, name={self.name!r})"
    
user1 = User(34, "Rahul")
user2 = User(35, "Priyanka")

print(f"User 1:\n"
      f"{user1}")
print(f"User 2:\n"
      f"{user2}")

# Output (with !r)
# User 1:
# User(user_id=34, name='Rahul')
# User 2:
# User(user_id=35, name='Priyanka')


# Output (without !r) => Rahul etc will look like a variable, they should looked like string values. Using !r will be good practise.
# User 1:
# User(user_id=34, name=Rahul)
# User 2:
# User(user_id=35, name=Priyanka)    

'''
# Key Points (Solution)
- Defines a User class with attributes: user_id and name.
- Implements __repr__ only, as required (no __str__).
- __repr__ returns a clear, unambiguous string representation.
- Uses f-string with !r to show name as a proper string literal.

# Key Points (Why __repr__ Is Important)
- __repr__ controls how objects appear during debugging.
- It is used automatically by:
  - print(object)
  - lists, tuples, dicts containing the object
- Helps developers understand object state instantly.

# Key Points (Design Details)
- __repr__ always returns a string.
- Output resembles valid constructor-style representation.
- !r calls repr() on name, making strings explicit and safe.

# Key Points (Behavior)
- Printing a single User shows meaningful details.
- Printing a list of User objects shows readable output.
- No ambiguity between variables and string values.

# Core Takeaway
- __repr__ is for developers, debugging, and containers.
- A good __repr__ makes objects self-explanatory.
- This is a best practice for all non-trivial classes.
'''
