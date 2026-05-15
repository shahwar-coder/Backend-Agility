'''
Question 3 — Multiple Decorators on an API
An API endpoint uses multiple decorators:

@rate_limit
@auth_required
def create_order(user, product_id):
    """Create a new order"""
    pass

Question:
What common change must be applied inside both decorators so that
the function name and docstring of create_order remain intact?
'''

from functools import wraps
from typing import Dict

# Decorator 1
def rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # rate limiting logic
        return func(*args, **kwargs)
    return wrapper

# Decorator 2
def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = args[0] # will have user details, a Dict
        if not user.get("is_authenticated"):
            return "401 Unauthorised"
        return func(*args, **kwargs)
    return wrapper

@rate_limit
@auth_required
def create_order(user: Dict, product_id: int):
    """Create a new order"""
    return f"Order created for product {product_id}"

# Authenticated user
user = {"is_authenticated": True}
print(create_order(user, 101))
# Output: Order created for product 101

# Unauthenticated user
user = {"is_authenticated": False}
print(create_order(user, 101))
# Output: 401 Unauthorized


'''
# Key Points (Solution)
- When multiple decorators are applied, each decorator wraps the function.
- Without special handling, metadata like __name__ and __doc__ is lost.
- functools.wraps(func) must be used inside every decorator.
- @wraps copies the original function’s name, docstring, and metadata.
- Both rate_limit and auth_required correctly apply @wraps(func).
- This ensures create_order keeps its identity across decorator layers.

# Key Points (Why This Matters)
- Preserves function name for logs, debuggers, and stack traces.
- Preserves docstring for documentation tools and help().
- Ensures frameworks (FastAPI, Flask, Django) work correctly.
- Critical when multiple decorators are stacked.

# Key Points (Output Behavior)
- Authenticated user → function executes normally.
- Unauthenticated user → authentication decorator blocks execution.
- Function name and docstring remain intact despite multiple decorators.

# Important Note
- @wraps is NOT optional in production-grade decorators.
- Every decorator in the stack must apply @wraps(func), not just one.
'''
