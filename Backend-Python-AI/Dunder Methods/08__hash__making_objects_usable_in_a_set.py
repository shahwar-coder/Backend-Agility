'''
TASK 1: MAKING OBJECTS USABLE IN A SET

Write a class `User` with:
- Attributes: id and email
- A __eq__ method that considers two Users equal
  when their id is the same
- A __hash__ method that makes this object usable
  inside a set or as a dictionary key

TEST CASES TO CONSIDER:
- Two User objects with the same id should behave
  as a single element in a set

RULES:
- __hash__ must be consistent with __eq__
- Do NOT use object memory address

GOAL:
Understand why __hash__ is required when __eq__ is overridden.
'''

# With not __hash__ (let's see the problem)
class User:
    """Blueprint for Users"""

    def __init__(self, user_id: str, email: str) -> None:
        self.user_id = user_id
        self.email = email

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, email={self.email!r})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id


user1 = User("AZ123", "alam@gmail.com")
user2 = User("AZ123", "other@gmail.com")

users_set = {user1, user2}
print(users_set)

# Actually you will get TypeError: unhashable type: 'User'
# Because Python since has not hash implemented so by default it won't allow the usage nside set and dict


# SAFE and CORRECTED (with __hash__)

class User:
    """Blueprint for Users"""

    def __init__(self, user_id: str, email: str) -> None:
        self.user_id = user_id
        self.email = email

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, email={self.email!r})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id

    def __hash__(self) -> int:
        return hash(self.user_id)


user1 = User("AZ123", "alam@gmail.com")
user2 = User("AZ123", "other@gmail.com")

users_set = {user1, user2}
print(users_set)
print(len(users_set))

# {User(user_id='AZ123', email='alam@gmail.com')}
# 1
# means deduplication worked


'''
# Key Points (What This Task Demonstrates)
- Overriding __eq__ changes how Python defines equality.
- Once __eq__ is overridden, Python disables the default __hash__.
- Without __hash__, objects become UNHASHABLE.
- Unhashable objects cannot be used in:
  - set
  - dict keys

# Key Points (Why the Error Happens)
- set/dict require hashing.
- Python protects you from broken hashing logic.
- If equality is custom, hashing must also be explicit.
- Hence: TypeError: unhashable type: 'User'

# Key Points (Correct Fix)
- __eq__ defines logical equality (same user_id).
- __hash__ defines bucket placement (hash(user_id)).
- Both must use the SAME identity attribute.

# Key Points (Consistency Rule)
- Equality rule:
    user1 == user2  ⇨  user1.user_id == user2.user_id
- Hash rule:
    hash(user1) == hash(user2) ⇨ hash(user_id)

- This satisfies Python’s contract:
    if a == b → hash(a) == hash(b)

# Key Points (Behavior After Fix)
- Two User objects with same user_id:
  - Compare equal
  - Produce same hash
  - Deduplicate correctly in a set
- Set length becomes 1, as expected.

# Backend Perspective
- This pattern is EXTREMELY common for:
  - Entity models
  - ORM objects
  - Cache keys
  - Deduplication logic
- user_id represents identity, email is metadata.

# Core Takeaway (Golden Rule)
- If you override __eq__,
  you MUST think about __hash__.
- Equality + hashing must describe the SAME identity.
- Otherwise, sets and dicts WILL break.
'''
