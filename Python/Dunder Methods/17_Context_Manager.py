'''
TASK: FILE LOGGER CONTEXT MANAGER

Design a context manager class `FileLogger` that:
- Accepts a file name during initialization
- Opens the file in append mode inside __enter__
- Returns the file object so it can be written to
- Closes the file inside __exit__

TEST CASE:
Use it like this:

with FileLogger("app.log") as f:
    f.write("User logged in\n")

RULES:
- Implement __enter__ and __exit__
- Do not open or close the file outside the context manager
- Ensure the file always closes after the with block

GOAL:
Understand how to design a custom context manager
that safely manages resources.
'''

class FileLogger:
    """Context manager for safe file logging."""

    def __init__(self, file_name: str) -> None:
        if not file_name:
            raise ValueError("File name cannot be empty")
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        # Open file in append mode
        self.file = open(self.file_name, "a", encoding="utf-8")
        return self.file  # return file object for writing

    def __exit__(self, exc_type, exc_value, traceback):
        # Ensure file is closed
        if self.file and not self.file.closed:
            self.file.close()
        # Do not suppress exceptions
        return False


# ---- Test case ----
with FileLogger("app.log") as f:
    f.write("User logged in\n")


with FileLogger("app.log") as f:
    f.write("User logged in\n")


'''
# Key Points (What This Implementation Demonstrates)
- Defines a FileLogger class as a custom context manager.
- Accepts a file name during initialization.
- Implements __enter__ and __exit__ to manage file resources safely.

# Key Points (How It Works)
- __enter__:
  - Opens the file in append mode ("a").
  - Stores the file object.
  - Returns the file so it can be written to.
- Code inside the with block writes to the file.
- __exit__:
  - Always closes the file after the block ends.
  - Runs whether the block succeeds or raises an error.

# Key Points (Safety Guarantees)
- File is never left open accidentally.
- Prevents resource leaks.
- Ensures proper cleanup even during exceptions.

# Key Points (Exception Behavior)
- __exit__ returns False.
- This means:
  - Exceptions are NOT suppressed.
  - Errors propagate normally (standard behavior).

# Backend / Real-World Use Cases
- Logging systems
- Temporary file handling
- Report generation
- Audit trails
- Any resource that must be closed reliably

# Core Takeaway
- Context managers automate resource management.
- __enter__ acquires the resource.
- __exit__ releases the resource.
- with statement guarantees cleanup.
'''
