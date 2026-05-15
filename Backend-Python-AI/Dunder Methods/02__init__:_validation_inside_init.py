'''
TASK 2: VALIDATION INSIDE __init__

Write a class `Account` with an __init__ method that:
- Accepts `balance`
- Raises ValueError if balance is negative
- Stores the balance only if it is valid
- Create one valid object and attempt to create one invalid object

RULES:
- Perform validation inside __init__
- Do NOT modify attributes after object creation

GOAL:
Understand how __init__ prepares an object
and prevents invalid state at creation time.
'''

class Account:
    def __init__(self, balance):
        if balance<0:
            raise ValueError("Balance can not be negative")
        self.balance = balance

    
# Valid account
account1 = Account(14000)
print(f"Acc Balance:\n"
      f"{account1.balance}")
# Acc Balance:
# 14000


try:
    account2 = Account(-500)
except ValueError as err:
    print(f"Error creaing account: {err}")

# Error creaing account: Balance can not be negative

'''
# Key Points (Solution)
- Defines an Account class with validation inside __init__.
- __init__ accepts balance as input.
- Immediately checks for invalid (negative) balance.
- Raises ValueError before object state is set.
- Stores balance only if it passes validation.

# Key Points (Why Validation Belongs in __init__)
- Prevents creation of invalid objects.
- Ensures every Account instance is always in a valid state.
- Eliminates need for defensive checks elsewhere in the code.
- Enforces invariants at the point of object creation.

# Key Points (Behavior Demonstrated)
- Valid account is created successfully.
- Invalid account creation fails immediately.
- No partially initialized object exists for invalid input.

# Key Points (Design Principle)
- Objects should never exist in an invalid state.
- __init__ is the correct place for construction-time validation.
- Fail fast → easier debugging and safer systems.

# Core Takeaway
- __init__ does not just assign values.
- It is responsible for protecting object integrity.
'''
