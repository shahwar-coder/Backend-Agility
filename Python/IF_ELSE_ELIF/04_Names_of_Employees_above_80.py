'''
14. Check if there is any employee above 80 years and print their name.
'''

import json
from typing import List, Dict, Generator


def load_employees(file_path: str) -> List[Dict]:
    try:
        with open(file_path, "r") as file:
            employees = json.load(file)

        if not isinstance(employees, list):
            raise ValueError("Employee data must be a list")

        return employees

    except FileNotFoundError as err:
        raise FileNotFoundError(f"File not found: {file_path}") from err

    except json.JSONDecodeError as err:
        raise ValueError("Invalid JSON format") from err


def employees_above_80(employees: List[Dict]) -> Generator[str, None, None]:
    for employee in employees:

        # Type validation
        if not isinstance(employee, dict):
            continue

        name = employee.get("ename")
        age = employee.get("age")

        if not isinstance(name, str) or not isinstance(age, (int, float)):
            continue

        # Domain validation
        if not name or age < 0:
            continue

        # Business logic
        if age > 80:
            yield name


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")

        found = False
        for name in employees_above_80(employees):
            print("Employees above 80 are: ")
            print(f"{name}")
            found = True

        if not found:
            print("No employee above 80 years found.")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Employees above 80 are: 
# Amitabh Bachchan

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Validates that the data is a list of dictionaries.
- Uses a generator to find employees above a given age.
- Safely extracts and validates name and age fields.
- Applies the condition age > 80 to identify very senior employees.
- Skips invalid or malformed employee records.
- Uses a flag to check whether any matching employee exists.
- Separates data loading, filtering logic, and output handling.

# Key Points (Output)
- Prints names of employees whose age is above 80.
- If none are found, prints an appropriate message.
- Output depends on the employee dataset.
- Example output:
  Employees above 80 are:
  Amitabh Bachchan

# Important Note
- Generators allow early stopping and efficient iteration.
- A flag is useful when conditional summary messages are required.
'''
