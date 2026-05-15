'''
2️⃣ Authentication – User Profile
You have:

def view_profile(user, is_logged_in):
    return f"Profile of {user}"

Task:
Apply the login_required decorator without modifying the function.
'''

from functools import wraps
from typing import Any

def login_required(func):
    '''Login Required Decorator'''
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        '''Wrapper'''
        is_logged_in = kwargs.get("is_logged_in") # login status is extracted from kwargs (keyword argument), we cannot go ahead and index desired parameter from args if the values are passed to args.

        # in case vlaues not provided via kwargs, we can fallback to args (the last resort)
        if is_logged_in is None and len(args)>=2:
            is_logged_in = args[1]

        if not is_logged_in:
            return "Please login to continue"
        return func(*args, **kwargs)
    
    return wrapper

@login_required
def view_profile(user, is_logged_in):
    return f"Profile of {user}"

print(view_profile("Shahwar", is_logged_in=True)) # Profile of Shahwar
print(view_profile("Shahwar", is_logged_in=False)) # Please login to continue


'''
# Key Points (Solution)
- Applies authentication using a decorator without modifying the original function.
- Uses @wraps(func) to preserve function metadata.
- Wrapper accepts *args and **kwargs for flexibility.
- Extracts is_logged_in safely from kwargs first.
- Falls back to args if is_logged_in is not provided as a keyword.
- Blocks access when user is not logged in.
- Allows normal execution when authentication passes.

# Key Points (Why This Approach Works)
- Does not depend on hardcoded argument positions.
- Works with both positional and keyword arguments.
- Keeps the original function signature untouched.
- Maintains compatibility with logging, debugging, and documentation tools.

# Key Points (Output)
- Logged-in user → profile is displayed.
- Not logged-in user → access is denied.
- Example outputs:
  Profile of Shahwar
  Please login to continue

# Important Note
- Flexible decorators are essential in real backend APIs.
- @wraps is mandatory for production-grade decorators.
'''
