'''
TASK 2: HUMAN-READABLE STATUS MESSAGE

Write a class `Server` with:
- Attributes: name and status
- A __str__ method that returns a readable sentence like:
  "Server Alpha is running"

TEST CASE:
- Create two Server objects with different statuses
- Print both objects to see the custom messages

RULES:
- __str__ should return a clear, human-friendly string
- Do not include technical or debug-style formatting

GOAL:
Learn how __str__ is used for clean, user-facing output.
'''

class Server:
    """Server with human-readable status"""

    def __init__(self, name: str, status: str) -> None:
        self.name = name
        self.status = status

    def __str__(self) -> str:
        """User-friendly server status message"""
        return f"Server {self.name} is {self.status}"


# Test cases
server1 = Server("Alpha", "running")
server2 = Server("Beta", "down")

print(server1)
print(server2)
