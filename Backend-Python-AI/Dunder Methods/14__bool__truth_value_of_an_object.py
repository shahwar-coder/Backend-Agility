'''
TASK: TRUTH VALUE OF AN OBJECT

Write a class `TaskQueue` that:
- Accepts a list of tasks during initialization
- Stores them as an instance attribute
- Implements a __bool__ method that:
  - Returns True if there is at least one task
  - Returns False if the task list is empty

TEST CASE:
- Create one TaskQueue with tasks → should be True in an if condition
- Create another with an empty list → should be False

RULES:
- Implement __bool__ only
- Do not check the list directly outside the class

GOAL:
Understand how objects control their truth value
when used in conditions like: if queue:
'''
from typing import List, Any


class TaskQueue:
    """Queue that holds tasks and defines its own truth value."""

    def __init__(self, tasks: List[Any]) -> None:
        if tasks is None:
            raise ValueError("Tasks cannot be None")
        if not isinstance(tasks, list):
            raise TypeError("Tasks must be a list")

        self.tasks = tasks

    def __bool__(self) -> bool:
        """Return True if there is at least one task."""
        return len(self.tasks) > 0


# ---- Test cases ----
tasks1 = TaskQueue(["task1", "task2", "task3"])
tasks2 = TaskQueue([])

if tasks1:
    print("Set of Tasks to be done!")
else:
    print("No task to be done.")

if tasks2:
    print("Set of Tasks to be done!")
else:
    print("No task to be done.")


# Set of Tasks to be done!
# No task to be done.

'''
# Key Points (What This Implementation Demonstrates)
- Defines a TaskQueue class that controls its own truth value.
- Accepts a list of tasks during initialization.
- Stores tasks as an instance attribute.
- Implements __bool__ to define how the object behaves in conditions.

# Key Points (How Truth Value Works)
- When Python evaluates:
    if queue:
  it internally calls:
    queue.__bool__()
- The returned boolean determines the branch taken.

# Key Points (Logic Used)
- __bool__ returns:
    True  → if there is at least one task
    False → if the task list is empty
- Uses:
    len(self.tasks) > 0
  as the condition.

# Key Points (Behavior in Test Cases)
- TaskQueue(["task1", "task2", "task3"]) → True
- TaskQueue([]) → False
- Conditional logic responds accordingly.

# Backend / Design Perspective
- Useful for:
  - job queues
  - message buffers
  - processing pipelines
- Enables clean, readable code:
    if task_queue:
        process_tasks()

# Core Takeaway
- Objects can define their own truth value.
- if obj: → calls obj.__bool__().
- This allows custom classes to behave naturally
  in conditional statements.
'''
