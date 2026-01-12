'''
4️⃣ Logging – Product Listing API

You have:

python
def list_products(category):
    return f"Products in {category}"

Task:
Write a decorator that logs:

Calling list_products with category=<value>
before execution.
'''


from functools import wraps
from typing import Any

def log_call(func):
    """Logs function name and category before execution"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        # extract category safely
        category = kwargs.get("category")
        if category is None and len(args) >= 1:
            category = args[0]

        print(f"Calling {func.__name__} with category={category}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def list_products(category):
    return f"Products in {category}"


# ---- Calls ----
print(list_products("Electronics"))
print(list_products(category="Books"))


# Calling list_products with category=Electronics
# Products in Electronics
# Calling list_products with category=Books
# Products in Books


'''
# Key Points (Solution)
- Uses a decorator to add logging without changing the function.
- @wraps(func) preserves function name and metadata.
- Wrapper accepts *args and **kwargs for flexibility.
- Safely extracts the category from kwargs first.
- Falls back to positional args if needed.
- Logs function name and category before execution.
- Executes the original function after logging.

# Key Points (Output)
- Logs are printed before the function runs.
- Function behavior and return value remain unchanged.
- Works with both positional and keyword arguments.
- Example log:
  Calling list_products with category=Electronics

# Important Note
- Logging decorators are common in backend APIs.
- Using flexible argument handling avoids tight coupling
  to function signatures.
'''
