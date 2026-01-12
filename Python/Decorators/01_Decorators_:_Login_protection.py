'''
1️⃣ Authentication – Orders Page
You have an API handler function:

def view_orders(user, is_logged_in):
    return "Orders data"

Task:
Create a decorator login_required that allows this function to run only if is_logged_in=True. Otherwise, return "Please login to continue".    
'''

def login_required(func):
    def wrapper(user, is_logged_in):
        if is_logged_in:
            return func(user, is_logged_in)
        else:
            return "Please login to continue"
    return wrapper

@login_required
def view_orders(user, is_logged_in):
    return "Orders Data"

print(view_orders("Shahwar", True))