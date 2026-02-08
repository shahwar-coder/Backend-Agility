'''
TASK: SIMPLE CONTEXT MANAGER

Write a class `DatabaseConnection` that:
- Accepts a database name during initialization
- Implements __enter__ to:
  - Print "Connecting to <database name>"
  - Return the object itself
- Implements __exit__ to:
  - Print "Closing connection to <database name>"

TEST CASE:
- Use the class with a `with` statement
- Ensure the connect message appears at the start
- Ensure the close message appears at the end

RULES:
- Implement both __enter__ and __exit__
- Do not manually call these methods

GOAL:
Understand how context managers work
with the `with` statement in Python.
'''

class DatabaseConnection:
    """Simple database connection context manager."""

    def __init__(self, db_name: str) -> None:
        if not db_name:
            raise ValueError("Database name cannot be empty")
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        return self  # must return the object

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing connection to {self.db_name}")
        # Returning False lets exceptions propagate (standard behavior)
        return False


# ---- Test case ----
with DatabaseConnection("ShahwarDB") as db:
    print("Inside context:", db.db_name)


# Connecting to ShahwarDB
# Inside context: ShahwarDB
# Closing connection to ShahwarDB

'''
# Key Points (What This Implementation Demonstrates)
- Defines a DatabaseConnection class as a context manager.
- Implements both __enter__ and __exit__ methods.
- Allows the object to be used with the `with` statement.

# Key Points (How the with Statement Works)
- When execution enters the with block:
    __enter__() is called.
- Its return value is assigned to the variable after `as`.
- When the block finishes (normally or with error):
    __exit__() is called automatically.

# Key Points (Behavior in This Example)
- __enter__:
  - Prints connection message.
  - Returns the object itself.
- Code inside the with block runs.
- __exit__:
  - Prints closing message.
  - Runs even if an error occurs.

# Key Points (Exception Handling Rule)
- __exit__ receives:
    exc_type, exc_value, traceback
- Returning False:
  - Does NOT suppress exceptions.
  - Allows them to propagate normally.
- This is the standard, safe behavior.

# Backend / Real-World Perspective
- Context managers are used for:
  - Database connections
  - File handling
  - Network sockets
  - Locks and transactions
- They guarantee cleanup even if errors occur.

# Core Takeaway
- with statement = automatic setup and cleanup.
- __enter__ → resource acquisition.
- __exit__ → resource release.
- Ensures safe, predictable resource handling.
'''
