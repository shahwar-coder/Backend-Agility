'''
6️⃣ Request Counter – Product Views

You have:

python
def view_product(product_id):
    return f"Product {product_id}"

Task:
Create a decorator that counts and prints how many times this API is called.
'''

from functools import wraps
from typing import Any

def request_counter(func):
    """Decorator to count how many times an API is called"""
    count = 0  # closure variable

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        nonlocal count
        count += 1
        print(f"{func.__name__} called {count} times")
        return func(*args, **kwargs)

    return wrapper


@request_counter
def view_product(product_id):
    return f"Product {product_id}"


# ---- Calls ----
print(view_product(101))
print(view_product(102))
print(view_product(103))


'''
# Key Points (Solution)
- Uses a decorator to track how many times a function is called.
- Maintains state using a closure variable (count).
- nonlocal keyword allows updating the outer variable inside wrapper.
- @wraps(func) preserves the original function’s metadata.
- Counter increments on every function invocation.
- Prints call count before executing the original function.
- Original function logic remains unchanged.

# Key Points (Output)
- Prints the call count each time the API is invoked.
- Counter increases sequentially across calls.
- Function return value is unaffected.
- Example output:
  view_product called 1 times
  view_product called 2 times
  view_product called 3 times

# Important Note
- Closure-based counters are simple and effective.
- In real backend systems, counters are often stored
  in shared stores (Redis, DB) for multi-instance setups.
'''

# NONLOCAL

'''
Q. Where is nonlocal used?
Ans. Only in nested functions.

Example structure:

def outer():
    x = 0      # nonlocal for inner

    def inner():
        nonlocal x
        x += 1

Here:
• x is local to outer
• inner() can read x without nonlocal
• but to modify x, nonlocal is mandatory
'''

# What's Closure:

'''
Key points (in our decorator code)

- count is created once when the decorator runs
- wrapper() is called many times
- count must persist across calls

This persistence is called a closure.
'''