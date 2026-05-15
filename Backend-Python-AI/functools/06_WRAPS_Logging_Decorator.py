'''
Question 1 — Logging Decorator
A backend service uses a logging decorator:

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

This decorator is applied to multiple API functions.

Question:
What change should be made to this decorator so that,
the original function’s name and docstring are preserved after decoration?
'''

from functools import wraps
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function Name : {wrapper.__name__}")
        print(f"Docstring     : {wrapper.__doc__}")
        print(f"Annotations   : {wrapper.__annotations__}")
        return func(*args, **kwargs)
    return wrapper

# example func
@log_call
def create_order(order_id: int):
    """Create a new order for the user"""
    return f"Order with ID: {order_id} created"

# call
print(create_order(1234567))

# >>>>---- Output (when no Decorator) ----<<<<
# Order with ID: 1234567 created

# >>>>---- Output (when Decorator is used) ----<<<<
# Function Name : create_order
# Docstring     : Create a new order for the user
# Annotations   : {'order_id': <class 'int'>}
# Order with ID: 1234567 created
# (So here we see meta data of the original function is preserved)


# =========================================================
# Know that:
# @wraps(func) copies metadata from func → wrapper, mainly:
# __name__
# __doc__
# __module__
# __annotations__
# __wrapped__ (very important for introspection)
# So now, the decorated function itself behaves like the original.



'''
# Key Points (Solution)
- The decorator must use functools.wraps(func).
- @wraps(func) is applied directly above the wrapper function.
- It copies metadata from the original function to the wrapper.
- Preserves __name__, __doc__, __annotations__, and __wrapped__.
- Logging now reflects the original function, not the wrapper.
- Business logic of the decorator remains unchanged.

# Key Points (Why This Change Is Needed)
- Without @wraps, the function name becomes "wrapper".
- Docstrings are lost, breaking documentation and help().
- Logs and debuggers show incorrect function identities.
- Backend frameworks rely on correct metadata for routing and introspection.

# Key Points (Observed Output)
- Printed function name matches the original function.
- Docstring and annotations are preserved correctly.
- Function execution works as expected.
- Example:
  Function Name : create_order
  Docstring     : Create a new order for the user

# Important Note
- @wraps is mandatory for production decorators.
- Every decorator in a stack must apply @wraps(func).
- __wrapped__ enables advanced introspection and decorator unwrapping.
'''
