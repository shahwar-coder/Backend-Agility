'''
TASK 2: VALUE-BASED OBJECT COMPARISON

Write a class `User` with:
- Attributes: id and email
- An __eq__ method that returns True when
  two User objects have the same id and email

TEST CASES TO CONSIDER:
- Two different User objects with same values → equal
- Objects with different values → not equal

RULES:
- Implement __eq__ only
- Return a boolean
- Do not compare object memory addresses

GOAL:
Understand how __eq__ enables value-based equality
instead of identity-based comparison.
'''

class User:
    "Users"
    def __init__(self, user_id: str, email: str)->None:
        self.user_id = user_id
        self.email = email

    def __repr__(self)->str:
        return f"User(uswr_id={self.user_id!r}, email={self.email!r})"
    
    def __eq__(self, other):
        if not isinstance(other, User):
            raise ValueError("Only same type entities can be compared")
        return self.user_id==other.user_id and self.email==other.email
    
# Test 1: Different values → NOT equal
user1 = User("A123Z", "aa@gmail.com")
user2 = User("Z123A", "bb@gmail.com")

print(user1 == user2)  # False

# Test 2: Same values → equal
user3 = User("A123Z", "aa@gmail.com")
user4 = User("A123Z", "aa@gmail.com")

print(user3 == user4)  # True


'''
# Key Points (What This Implementation Achieves)
- Implements value-based equality using __eq__.
- Two User objects are considered equal only if:
  - user_id is the same
  - email is the same
- Equality depends on data, not memory address.
- Demonstrates correct comparison semantics for domain objects.

# Key Points (Behavior Explained)
- user1 == user2 → False
  - Different user_id and email.
- user3 == user4 → True
  - Same user_id and same email.
- Objects are different instances, but logically equal.

# Key Points (Why __eq__ Is Important)
- Enables meaningful comparisons in business logic.
- Required for:
  - deduplication
  - list comparisons
  - testing
  - domain correctness
- Shifts comparison from identity-based to value-based.

# Important Correction (Very Subtle but Critical)
- In __eq__, this line:
    if not isinstance(self, User):
  should conceptually be:
    if not isinstance(other, User):

- Reason:
  - self is *always* a User inside User.__eq__
  - We must validate the type of the object being compared *against*

- Best practice:
  - Return NotImplemented (not raise ValueError)
  - This allows Python to handle unsupported comparisons correctly

# Correct Mental Model
- __eq__ answers:
  “Do these two objects represent the same value/entity?”
- Identity (memory address) is irrelevant here.

# Core Takeaway
- __eq__ defines logical equality.
- Value-based equality is foundational in backend models.
- Small mistakes in __eq__ can silently break comparisons,
  so precision here matters a lot.
'''

'''
# Key Points (What This Implementation Demonstrates)
- Implements partial equality using __eq__.
- Equality is based ONLY on user_id.
- email is intentionally ignored during comparison.
- Two User objects with the same user_id are considered equal,
  regardless of email differences.

# Key Points (Why This Is Valid and Useful)
- In many backend systems, user_id is the true identity.
- email may change over time, user_id should not.
- Equality reflects business identity, not full state.

# Key Points (Correct __eq__ Pattern)
- Checks type of `other`, not `self`.
- Returns NotImplemented for unsupported comparisons.
- Returns a boolean result for valid comparisons.

# Key Points (Behavior Explained)
- Same user_id → equal (True)
- Different user_id → not equal (False)
- Memory addresses are irrelevant.

# Design Implications
- Objects that compare equal should represent the same entity.
- This equality logic affects:
  - deduplication
  - set membership
  - dictionary keys (if __hash__ is defined)
- Equality rules must align with domain invariants.

# Core Takeaway
- __eq__ defines *what equality means* for your object.
- Equality does NOT have to include all attributes.
- Partial equality is common and intentional in backend models.
'''
