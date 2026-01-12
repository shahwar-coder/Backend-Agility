'''
8️⃣ Method Guard – Delete Product API

You have:

def delete_product(product_id, method):
    return "Product deleted"

Task:
Create a decorator that allows execution only if method="DELETE".
'''

from functools import wraps
from typing import Any

def allow_delete_only(func):
    """Decorator to allow execution only for HTTP DELETE method"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        # Prefer keyword argument
        method = kwargs.get("method")

        # Positional fallback: (product_id, method)
        if method is None and len(args) >= 2:
            method = args[1]

        # Guard check
        if not isinstance(method, str) or method.upper() != "DELETE":
            return "Method Not Allowed"

        return func(*args, **kwargs)
    return wrapper


@allow_delete_only
def delete_product(product_id, method):
    return "Product deleted"


# ---- Calls ----
print(delete_product(101, "DELETE"))     # Product deleted
print(delete_product(101, "POST"))       # Method Not Allowed
print(delete_product(101, method="delete"))  # Product deleted
