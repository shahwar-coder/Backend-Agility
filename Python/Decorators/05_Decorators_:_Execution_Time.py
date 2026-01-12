'''
5️⃣ Execution Time – Checkout API

You have:

python
def checkout(cart_id):
    return "Checkout successful"

Task:
Create a decorator that prints how long the checkout function takes to execute.
'''

import time
from functools import wraps
from typing import Any


def measure_execution_time(func):
    """Decorator to measure and print execution time of a function"""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {(end_time - start_time):.6f} seconds")
        return result
    return wrapper


@measure_execution_time
def checkout(cart_id):
    return "Checkout successful"


# ---- Call ----
print(checkout("CART123"))

# checkout executed in 0.000001 seconds
# Checkout successful

'''
# Key Points (Solution)
- Uses a decorator to measure function execution time.
- @wraps(func) preserves the original function’s metadata.
- time.perf_counter() provides high-precision timing.
- Records start time before function execution.
- Records end time after function execution.
- Calculates elapsed time as end_time − start_time.
- Prints execution time along with the function name.
- Returns the original function’s result unchanged.

# Key Points (Output)
- Prints execution time in seconds (microsecond precision).
- Function result is printed normally after timing.
- Example output:
  checkout executed in 0.000002 seconds
  Checkout successful

# Important Note
- perf_counter() is preferred over time.time() for benchmarking.
- Timing decorators are commonly used for performance monitoring
  in backend services and APIs.
'''


