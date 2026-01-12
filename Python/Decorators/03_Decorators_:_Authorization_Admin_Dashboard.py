'''
3️⃣ Authorization – Admin Dashboard
You have:

def admin_dashboard(user, role):
    return "Admin dashboard data"

Task:
Create a decorator admin_only that allows execution only if role="admin", 
else return "Access denied".
'''

from functools import wraps
def admin_only(func):
    '''Admin Only Decorator'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        # always find in kwargs first
        role = kwargs.get("role")

        # in case kwargs does not have, use positions to extract the value
        if role is None and len(args)>=2:
            role = args[1]

        # logic
        if role.lower() == "admin":
            return func(*args, **kwargs)
        return "Access Denied"
    return wrapper

@admin_only
def admin_dashboard(user, role):
    return "Admin dashboard data"

print(admin_dashboard("Shahwar", "Admin")) # Admin dashboard data
print(admin_dashboard("Shahwar", "Staff")) # Access Denied