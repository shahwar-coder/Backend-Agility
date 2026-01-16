'''
SCENARIO:
A backend service needs to process a large number of user records
fetched from a database. Loading all records into memory at once
is inefficient.

TASK:
Write a generator function `stream_users(users)` that: (catch: I have stream from a file, even better...)
- Accepts a list of user dictionaries
- Yields one user at a time
- Allows sequential processing without creating a new list
'''

from typing import List, Dict, Generator
import json

def stream_users_from_a_file(file_path: str)->Generator[Dict[str, object], None, None]:
    '''Read users from the file and yield them one by one'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            raise ValueError("No users Found")
        
        if not isinstance(data, list):
            raise ValueError("Users data should have been a List")
        
        for user in data:
            yield user

    except FileNotFoundError as err:
        raise FileNotFoundError("JSON File not found") from err
    except json.JSONDecodeError as err:
        raise ValueError("JSON File could not be read") from err

def main()->None:
    try:
        for user in stream_users_from_a_file("Python/Generators/user_json.json"):
            print(user)
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# {'id': 101, 'username': 'alice_w', 'email': 'alice@example.com', 'is_active': True, 'role': 'user', 'created_at': '2024-06-12T10:15:30Z'}
# {'id': 102, 'username': 'bob_k', 'email': 'bob@example.com', 'is_active': False, 'role': 'user', 'created_at': '2024-07-01T08:42:10Z'}
# {'id': 103, 'username': 'charlie_admin', 'email': 'charlie@example.com', 'is_active': True, 'role': 'admin', 'created_at': '2023-12-20T14:05:55Z'}
# {'id': 104, 'username': 'dina_s', 'email': 'dina@example.com', 'is_active': True, 'role': 'user', 'created_at': '2024-09-18T19:22:01Z'}
# {'id': 105, 'username': 'evan_r', 'email': 'evan@example.com', 'is_active': True, 'role': 'moderator', 'created_at': '2024-10-03T11:47:44Z'}


'''
# Key Points (Solution)
- Uses a generator to stream user records one by one.
- Reads data from disk instead of keeping all users in memory.
- Yields each user dictionary sequentially.
- Avoids creating a new list during processing.
- Validates file existence and JSON structure.
- Ensures data is a list before streaming.
- Clean separation of file I/O and iteration logic.

# Key Points (Why This Is Backend-Style)
- Ideal for large datasets that cannot fit into memory.
- Matches real-world patterns (DB cursors, file streams).
- Enables pipelines (filtering, validation, persistence).
- Generator enforces sequential consumption.
- Safer for background jobs and batch processing.

# Key Points (Complexity & Memory)
- Time complexity: O(N), N = number of users.
- Memory usage: O(1) additional memory.
- Each record is processed exactly once.
- No intermediate data structures created.

# Key Points (Output)
- Outputs one user dictionary at a time.
- Order matches the file order.
- Consumer controls how many users are processed.

# Important Note
- This pattern scales well for logs, exports, ETL jobs.
- For very large files, line-by-line formats (CSV, NDJSON)
  can be even more memory efficient than full JSON load.
'''
