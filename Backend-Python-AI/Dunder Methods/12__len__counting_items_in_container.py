'''
TASK 1: COUNTING ITEMS IN A CONTAINER

Write a class `Cart` that:
- Accepts a list of items during initialization
- Stores them as an instance attribute
- Implements a __len__ method that returns
  the number of items in the cart

TEST CASE:
- Create a Cart with 3 items
- Call len(cart) and verify it returns 3

RULES:
- __len__ must return an integer
- Do not manually count items outside the class

GOAL:
Understand that len(obj) internally calls obj.__len__().
'''

from typing import List, Any


class Cart:
    """Shopping cart container"""

    def __init__(self, items: List[Any]) -> None:
        if items is None:
            raise ValueError("Items cannot be None")
        if not isinstance(items, list):
            raise TypeError("Items must be a list")

        self.items = items

    def __len__(self) -> int:
        """Return number of items in the cart"""
        return len(self.items)


# Test case
cart1 = Cart(["bag", "watch", "trolley", "t-shirt"])
print(len(cart1))  

# 4


'''
# Key Points (What This Implementation Demonstrates)
- Defines a Cart class that acts like a container.
- Accepts a list of items during initialization.
- Stores the items as an instance attribute.
- Implements __len__ to return the number of items.

# Key Points (How len(cart) Works)
- Calling len(cart) triggers:
    cart.__len__()
- Python internally uses the __len__ method.
- No need to manually count items outside the class.

# Key Points (Validation Logic)
- Prevents None from being passed as items.
- Ensures items is a list.
- Protects the object from invalid initial state.

# Key Points (Behavior)
- Cart created with 4 items.
- len(cart1) returns 4.
- Result matches the number of items stored.

# Backend / Design Perspective
- __len__ makes objects behave like containers.
- Useful for:
  - carts
  - queues
  - result sets
  - buffers
- Enables clean, Pythonic code:
    if len(cart) > 0:
        process(cart)

# Core Takeaway
- len(obj) → calls obj.__len__().
- Implementing __len__ makes custom objects
  behave like built-in containers.
'''
