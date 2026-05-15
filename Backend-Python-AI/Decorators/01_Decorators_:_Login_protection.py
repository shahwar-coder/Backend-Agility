'''
1️⃣ Authentication – Orders Page
You have an API handler function:

def view_orders(user, is_logged_in):
    return "Orders data"

Task:
Create a decorator login_required that allows this function to run only if is_logged_in=True. Otherwise, return "Please login to continue".    
'''
from functools import wraps
def login_required(func):
    @wraps(func)
    def wrapper(user, is_logged_in): # def wrapper(*args, **kwargs): , can be used for more safety in backend
        if not is_logged_in: # this is boolean check style, often better than nornal if else structure
            return "Please login to continue"
        return func(user, is_logged_in)
    return wrapper

@login_required
def view_orders(user, is_logged_in):
    return "Orders Data"

print(view_orders("Shahwar", True))

# Output:
# Orders Data


'''
# Key Points (Solution)
- Uses a decorator to enforce login checks.
- @wraps(func) preserves the original function’s metadata.
- Wrapper intercepts the call before the actual function runs.
- Checks the boolean is_logged_in flag.
- Allows execution only when is_logged_in is True.
- Returns an access message when authentication fails.
- Original function logic remains untouched.

# Key Points (Output)
- When is_logged_in=True → function executes normally.
- When is_logged_in=False → access is denied.
- Example output: Orders Data

# Important Note
- Using decorators keeps authentication logic reusable.
- For real backends, prefer *args and **kwargs for flexibility.
'''
