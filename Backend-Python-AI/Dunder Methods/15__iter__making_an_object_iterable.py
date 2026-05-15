'''
TASK: MAKING AN OBJECT ITERABLE

Write a class `LogCollection` that:
- Accepts a list of log messages during initialization
- Stores them as an instance attribute
- Implements an __iter__ method that allows the object
  to be used in a for-loop

TEST CASE:
- Create a LogCollection with 3 log messages
- Use a for-loop to print each message

RULES:
- Implement __iter__ only
- Do not manually access the internal list outside the class

GOAL:
Understand that __iter__ makes an object iterable
and allows it to work with for-loops.
'''
from typing import List, Iterator
class LogCollection:
    def __init__(self, logs: List[str])->None:
        if logs is None:
            raise ValueError("No logs")
        if not isinstance(logs, list):
            raise TypeError("Logs empty")
        self.logs = logs

    def __iter__(self)->Iterator:
        return iter(self.logs)

logs = LogCollection(["log1", "log2", "log3"])

for i, log in enumerate(logs, start=1):
    print(f"Log {i} : {log}")

# Log 1 : log1
# Log 2 : log2
# Log 3 : log3

'''
# Key Points (What This Implementation Demonstrates)
- Defines a LogCollection class that behaves like an iterable.
- Accepts a list of log messages during initialization.
- Stores logs as an instance attribute.
- Implements __iter__ to make the object usable in for-loops.

# Key Points (How Iteration Works)
- When Python sees:
    for log in logs:
  it internally calls:
    logs.__iter__()
- __iter__ returns an iterator object.
- The loop then repeatedly calls next() on that iterator.

# Key Points (Implementation Choice)
- __iter__ returns:
    iter(self.logs)
- This reuses Python’s built-in list iterator.
- No need to manually implement iteration logic.

# Key Points (Behavior in Test Case)
- LogCollection holds 3 log messages.
- for-loop successfully iterates over them.
- enumerate adds numbering during iteration.

# Backend / Design Perspective
- Iterable objects are common in:
  - log streams
  - result sets
  - database cursors
  - message queues
- Makes custom objects behave like native containers.

# Core Takeaway
- __iter__ makes an object iterable.
- for-loop → calls __iter__ internally.
- Returning an existing iterator is the simplest,
  most Pythonic solution.
'''
