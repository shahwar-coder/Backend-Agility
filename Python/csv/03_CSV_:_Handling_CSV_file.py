# Similar construct or template to solve such problems
# Have a read...

'''
Question 3 — Handling CSV from External Sources (Backend Robustness)

A backend job reads CSV files uploaded by external clients.
Some rows may have missing values.

Write a function that:
- Reads a CSV file using the csv module
- Skips rows where required fields (id or email) are missing
- Logs or counts how many rows were skipped
- Returns valid rows only

Focus on:
Defensive CSV reading
Backend-style validation
Clean control flow
'''

import csv
from typing import List, Dict, Tuple

REQUIRED_FIELDS = {"id", "email"}

def load_valid_rows_from_csv(file_path: str) -> Tuple[List[Dict[str, str]], int]:
    """
    Read a CSV file and return valid rows only.
    Rows missing required fields are skipped and counted.
    """
    valid_rows: List[Dict[str, str]] = []
    skipped_count = 0

    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Defensive: empty or header-less file
            if not reader.fieldnames:
                raise ValueError("CSV file is empty or has no headers")

            for row in reader:
                if not row:
                    skipped_count += 1
                    continue

                # Required field validation
                if not REQUIRED_FIELDS.issubset(row.keys()):
                    skipped_count += 1
                    continue

                if not row.get("id") or not row.get("email"):
                    skipped_count += 1
                    continue

                valid_rows.append(row)

        return valid_rows, skipped_count

    except FileNotFoundError as err:
        raise FileNotFoundError("CSV file not found") from err
    except csv.Error as err:
        raise ValueError("Invalid CSV format") from err


def main() -> None:
    try:
        valid_users, skipped = load_valid_rows_from_csv("external_users.csv")

        print(f"Valid rows count   : {len(valid_users)}")
        print(f"Skipped rows count : {skipped}")

        for user in valid_users:
            print(user)

    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


'''
# Key Points (Solution)
- Uses csv.DictReader to read rows as dictionaries (column-name based).
- Avoids index-based access for robustness against column reordering.
- Validates that the CSV file has headers before processing.
- Defines REQUIRED_FIELDS to clearly express mandatory columns.
- Skips rows where required fields (id or email) are missing or empty.
- Counts skipped rows instead of failing the entire job.
- Collects only valid rows into a clean list of dictionaries.
- Returns both valid data and skipped count for reporting.

# Key Points (Why This Is Backend-Style)
- External uploads are untrusted and often malformed.
- Defensive validation prevents bad data from entering the system.
- Skipping invalid rows keeps batch jobs resilient.
- Counting skipped rows enables monitoring, alerts, and audit logs.
- Dict-based rows integrate easily with databases and APIs.

# Key Points (Control Flow Design)
- Early continues keep logic readable and flat.
- Clear separation of:
  - File I/O
  - Validation
  - Business rules
- Function returns structured results instead of printing internally.

# Key Points (Output)
- valid_rows → list of clean user dictionaries.
- skipped_count → integer representing rejected rows.
- Example output:
  Valid rows count   : 5
  Skipped rows count : 3

# Important Note
- This pattern is common in ETL pipelines and background jobs.
- For large files, this can be converted to a generator
  to stream valid rows instead of storing them all.
'''
