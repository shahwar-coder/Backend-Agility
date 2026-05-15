'''
TASK 1: PARTIAL EQUALITY USING __eq__

Write a class `User` with:
- Attributes: id and email
- An __eq__ method that returns True when
  two User objects have the SAME id
- Ignore the email field while comparing

TEST CASES TO CONSIDER:
- Same id, different emails → equal
- Different ids, same email → not equal

RULES:
- Implement __eq__ only
- Use value-based comparison
- Do not compare object identity (is)

GOAL:
Understand that __eq__ defines custom equality rules
and does not have to compare all attributes.
'''


class User:
    """Represents a user identified uniquely by user_id."""

    def __init__(self, user_id: str, email: str) -> None:
        self.user_id = user_id
        self.email = email

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, email={self.email!r})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return self.user_id == other.user_id


# ---- Test Cases ----

# Same id, different emails → equal
user1 = User("U1001", "alice@example.com")
user2 = User("U1001", "alice.work@example.com")

print(user1 == user2)  # True

# Different ids, same email → not equal
user3 = User("U2002", "shared@example.com")
user4 = User("U3003", "shared@example.com")

print(user3 == user4)  # False

