'''
Question 1 — Reading CSV Data Safely (Backend Input Handling)

A backend service receives a CSV file containing user data with headers:
id, name, email, is_active

Write a function that:

Uses Python’s csv module to read the file
Iterates over rows using column names (not indexes)
Collects only users where is_active is "true"
Returns the filtered users as a list of dictionaries

Focus on:

Using the correct CSV reader
Clean iteration
Backend-friendly data structure
'''

import csv
from typing import Generator, Dict

REQUIRED_HEADERS = {"id", "name", "email", "is_active"}

def stream_active_users(file_path: str)->Generator[Dict[str, str], None, None]:
    '''Load CSV file, Stream active users'''
    try:
        with open(file_path, 'r', newline="", encoding="utf-8") as file: # we are telling Python's open() to stay out of handling new lines, rather let csv module do it, otherwise we may have problems like empty lines between original lines.
            reader = csv.DictReader(file)

            # In-case empty file 
            if not reader.fieldnames:
                raise ValueError("CSV file is empty")
            
            # In-case missing required columns
            if not REQUIRED_HEADERS.issubset(reader.fieldnames):
                missing = REQUIRED_HEADERS - set(reader.fieldnames)
                raise ValueError(f"CSV missing required columns: {missing}")
            
            # In-case, large csv file, we stream rows
            for row in reader:
                if not row:
                    continue

                is_active = row.get("is_active", "").strip().lower()
                if is_active == "true":
                    yield row

    except FileNotFoundError as err:
        raise FileNotFoundError("CSV File not found") from err
    
    except csv.Error as err: # just like we have json decode error for errory json format, raise for format error is always ValueError.
        raise ValueError("Invalid CSV format")


def main()->None:
    try:
        print("Active Users:")
        for user in stream_active_users("Python/csv/users_csv.csv"):
            print(user)

    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Output:
# Active Users:
# {'id': '1', 'name': 'Aarav Sharma', 'email': 'aarav.sharma@example.com', 'is_active': 'true'}
# {'id': '3', 'name': 'Rohan Singh', 'email': 'rohan.singh@example.com', 'is_active': 'true'}
# {'id': '4', 'name': 'Priya Patel', 'email': 'priya.patel@example.com', 'is_active': 'true'}
# {'id': '6', 'name': 'Ananya Gupta', 'email': 'ananya.gupta@example.com', 'is_active': 'true'}
# {'id': '8', 'name': 'Sneha Iyer', 'email': 'sneha.iyer@example.com', 'is_active': 'true'}


'''
# Key Points (Solution)
- Uses csv.DictReader to read CSV rows as dictionaries (column-name based).
- Avoids index-based access, making the code resilient to column order changes.
- Opens file with newline="" so csv module handles line endings correctly.
- Validates that the CSV is not empty.
- Ensures required headers (id, name, email, is_active) are present.
- Streams rows using a generator to handle large CSV files efficiently.
- Filters only rows where is_active == "true" (case-insensitive).
- Yields dictionaries directly, making the output backend-friendly.

# Key Points (Why This Is Backend-Style)
- Streaming (generator) avoids loading entire files into memory.
- Header validation prevents silent data corruption.
- Dict-based rows integrate cleanly with APIs, DB layers, and serializers.
- Defensive checks handle malformed or unexpected input gracefully.
- Clean separation of I/O, validation, and business logic.

# Key Points (Output)
- Output is a stream (generator) of dictionaries.
- Each dictionary represents one active user.
- Only users with is_active = "true" are included.
- Example output:
  {'id': '1', 'name': 'Aarav Sharma', 'email': 'aarav.sharma@example.com', 'is_active': 'true'}

# Important Note
- csv.DictReader is preferred for backend CSV ingestion.
- This pattern scales well for background jobs and ETL pipelines.
'''
