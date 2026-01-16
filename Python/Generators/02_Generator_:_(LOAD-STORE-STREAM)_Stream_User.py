'''
SCENARIO:
A backend service needs to process a large number of user records
fetched from a database. Loading all records into memory at once
is inefficient.

TASK:
Write a generator function `stream_users(users)` that:
- Accepts a list of user dictionaries
- Yields one user at a time
- Allows sequential processing without creating a new list
'''

from typing import List, Dict, Generator
import json

def stream_users(users: List[Dict[str, object]])->Generator[Dict, None, None]:
    '''Stream users'''
    for user in users:
        yield user

def load_users_from_file(file_path: str)->List[Dict[str, object]]:
    '''Bring users'''
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        if not data:
            raise ValueError("No users Found")
        
        if not isinstance(data, list):
            raise ValueError("Users data should have been a List")
        
        return data # users is returned

    except FileNotFoundError as err:
        raise FileNotFoundError("JSON File not found") from err
    except json.JSONDecodeError as err:
        raise ValueError("JSON File could not be read") from err

def main()->None:
    try:
        users = load_users_from_file("Python/Generators/user_json.json")
        print("Users in the file:\n")
        for user in stream_users(users):
            print(user)
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# [ JSON FILE ] → [ FULL LIST IN MEMORY ] → generator iteration
# THIS IS PROBLEMATIC (avoid loading if possible or atleast avoid storing if you still have to load) -> meaning you are creating users =.... and then using it to stream, defeats generator benefit...
# Rather, directly on the fly, open file and start yielding the content..no need to store in the middle..
# Here, load could not be avoided, this is just json limitation, we don'y have any option but read the file here..


# Users in the file:

# {'id': 101, 'username': 'alice_w', 'email': 'alice@example.com', 'is_active': True, 'role': 'user', 'created_at': '2024-06-12T10:15:30Z'}
# {'id': 102, 'username': 'bob_k', 'email': 'bob@example.com', 'is_active': False, 'role': 'user', 'created_at': '2024-07-01T08:42:10Z'}
# {'id': 103, 'username': 'charlie_admin', 'email': 'charlie@example.com', 'is_active': True, 'role': 'admin', 'created_at': '2023-12-20T14:05:55Z'}
# {'id': 104, 'username': 'dina_s', 'email': 'dina@example.com', 'is_active': True, 'role': 'user', 'created_at': '2024-09-18T19:22:01Z'}
# {'id': 105, 'username': 'evan_r', 'email': 'evan@example.com', 'is_active': True, 'role': 'moderator', 'created_at': '2024-10-03T11:47:44Z'}


'''
# Key Points (Solution)
- Defines a generator function stream_users(users) that yields users one at a time.
- Generator does not create a new list; it reuses the existing iterable.
- Sequential processing is enabled via yield.
- Keeps iteration logic simple and explicit.
- Demonstrates correct generator syntax for backend-style streaming.

# Key Points (Design Trade-off Highlighted)
- JSON loading inherently loads the full file into memory.
- Calling json.load() returns a complete list → unavoidable with standard JSON.
- Passing that list to a generator does NOT reduce memory usage.
- Generator benefit here is iteration control, not memory savings.

# Key Points (Why This Matters in Backend Systems)
- Streaming from an in-memory list is still useful for:
  - Pipelines
  - Validation chains
  - Conditional early exits
- True memory efficiency requires streaming sources
  (DB cursors, CSV rows, NDJSON, API pagination).

# Key Points (Complexity & Memory)
- Time complexity: O(N), N = number of users.
- Memory usage: O(N) due to JSON load, O(1) during iteration.
- Each user is yielded exactly once.

# Important Note
- Generator ≠ memory efficiency by default.
- Memory efficiency depends on the data source, not yield alone.
- This example clearly shows a *correct generator* but also
  the *limitation of JSON as a storage format*.
'''
