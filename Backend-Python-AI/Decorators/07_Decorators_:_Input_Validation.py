'''
7️⃣ Input Validation – Price Update

You have:

def update_price(product_id, price):
    return "Price updated"

Task:
Create a decorator that blocks execution if price is negative or zero.
'''

from functools import wraps
from typing import Any

def validate_price(func):
    """Decorator to validate that price is positive"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        # Prefer kwargs first
        price = kwargs.get("price")

        # Positional fallback (product_id, price)
        if price is None and len(args) >= 2:
            price = args[1]

        # Validation
        if not isinstance(price, (int, float)) or price <= 0:
            return "Invalid price"

        return func(*args, **kwargs)
    return wrapper


@validate_price
def update_price(product_id, price):
    return "Price updated"


# ---- Calls ----
print(update_price(101, 500))     # Price updated
print(update_price(101, -50))     # Invalid price
print(update_price(101, price=0)) # Invalid price
