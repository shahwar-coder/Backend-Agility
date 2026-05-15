'''
Question 2 — Authentication Decorator
An authentication decorator is defined as:

def auth_required(func):
    def wrapper(user):
        if not user["is_authenticated"]:
            return "401 Unauthorized"
        return func(user)
    return wrapper

Question:
How should this decorator be modified 
to ensure backend logs and debuggers can still identify the original function correctly?
'''

from functools import wraps
from typing import Dict
def auth_required(func):
    @wraps(func)
    def wrapper(user):
        if not user["is_authenticated"]:
            return "401 Unauthorized"
        return func(user)
    return wrapper

@auth_required
def get_user_profile(user: Dict):
    """Display User Profile"""
    return "User Profile"

# When Authenticated
print(get_user_profile({
    "is_authenticated": True
}))
# Output: User Profile

# When not Authenticated
print(get_user_profile({
    "is_authenticated": False
}))
# Output: 401 Unauthorized



'''
# Key Points (Solution)
- The decorator must use functools.wraps(func).
- @wraps(func) is applied directly above the wrapper function.
- It copies metadata from the original function to the wrapper.
- Preserves __name__, __doc__, and other function attributes.
- Ensures the decorated function behaves transparently.

# Key Points (Why This Is Required)
- Backend logs rely on function names for traceability.
- Debuggers and stack traces need the original function identity.
- Documentation tools (help(), Swagger, OpenAPI) read docstrings.
- Frameworks like Flask/FastAPI expect correct metadata.

# Key Points (Decorator Behavior)
- If user is authenticated → original function executes.
- If not authenticated → returns "401 Unauthorized".
- Decoration does NOT alter business logic, only metadata handling.

# Important Note
- Every production decorator should use @wraps.
- Missing @wraps leads to confusing logs and harder debugging.
'''
