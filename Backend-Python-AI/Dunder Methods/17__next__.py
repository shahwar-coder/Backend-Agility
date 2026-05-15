'''
TASK: BUILDING A SIMPLE COUNTER ITERATOR

Write a class `Counter` that:
- Accepts a starting number and an ending number
- Implements __iter__ to return the object itself
- Implements __next__ to:
  - Return the next number in the sequence
  - Stop iteration when the end is reached

TEST CASE:
- Create Counter(1, 3)
- Use a for-loop to print numbers
- Output should be:
  1
  2
  3

RULES:
- Implement both __iter__ and __next__
- Raise StopIteration when the sequence ends

GOAL:
Understand how __next__ produces values
one at a time during iteration.
'''

class Counter:
    """Simple counter iterator from start to end (inclusive)."""

    def __init__(self, start: int, end: int) -> None:
        if start > end:
            raise ValueError("start must be less than or equal to end")
        self.current = start
        self.end = end

    def __iter__(self):
        # Iterator returns itself
        return self

    def __next__(self):
        # Stop condition
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1
        return value


# ---- Test case ----
counter = Counter(1, 3)

for number in counter:
    print(number)

# 1
# 2
# 3

'''
# Key Points (What This Code Demonstrates)
- A class-based iterator using __iter__ and __next__.
- Produces numbers from start to end (inclusive).
- Mimics how built-in iterators work in Python.

# How Iteration Works Here
- __iter__:
  - Returns the iterator object itself.
  - Required so Python can start iteration.

- __next__:
  - Returns the next value in the sequence.
  - Increments the internal counter.
  - Raises StopIteration when done.

# Execution Flow in for-loop
for number in counter:
    1. Python calls counter.__iter__()
    2. Repeatedly calls counter.__next__()
    3. Stops when StopIteration is raised

# Why This Is an Iterator (not just iterable)
- Object implements both:
  - __iter__()
  - __next__()
- So it is its own iterator.

# Core Takeaway
- __iter__ → prepares iteration
- __next__ → produces next value
- StopIteration → signals end of data
'''
