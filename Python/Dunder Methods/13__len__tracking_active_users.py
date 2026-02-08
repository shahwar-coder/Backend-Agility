'''
TASK 2: TRACKING ACTIVE USERS

Write a class `UserPool` that:
- Accepts a list of user dictionaries
- Only counts users where "is_active" is True
- Implements __len__ to return the number of active users

TEST CASE:
- Provide a mix of active and inactive users
- len(user_pool) should return only the active count

RULES:
- Filtering logic must be inside __len__
- __len__ must return an integer

GOAL:
Understand that __len__ can represent
a logical size, not just physical length.
'''

from typing import List, Dict, Any

class UserPool:
    """Container that tracks active users only"""

    def __init__(self, users: List[Dict[str, Any]]) -> None:
        if users is None:
            raise ValueError("Users cannot be None")
        if not isinstance(users, list):
            raise TypeError("Users must be a list of dictionaries")

        self.users = users

    def __len__(self) -> int:
        """Return number of active users"""
        active_count = 0

        for user in self.users:
            if not isinstance(user, dict):
                continue

            is_active = user.get("is_active")
            if is_active is True:
                active_count += 1

        return active_count


# ---- Test case ----
users_data = [
    {"id": 1, "name": "Rahul", "is_active": True},
    {"id": 2, "name": "Priya", "is_active": False},
    {"id": 3, "name": "Aman", "is_active": True},
    {"id": 4, "name": "Neha", "is_active": False},
    {"id": 5, "name": "Karan", "is_active": True},
]

user_pool = UserPool(users_data)

print(len(user_pool))

# Output: 3
