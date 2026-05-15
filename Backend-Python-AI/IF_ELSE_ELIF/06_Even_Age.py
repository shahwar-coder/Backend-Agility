"""
16. Print employees whose age is an even number.
"""

import json
from typing import List, Dict, Generator, Tuple, Union


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


def employees_with_even_age(
    employees: List[Dict],
) -> Generator[Tuple[str, Union[int, float]], None, None]:
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
        if int(age) % 2 == 0:
            yield name, age


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name, age in employees_with_even_age(employees):
            print(f"Name: {name}, Age: {age}")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Name: Deepika Padukone, Age: 38
# Name: Amitabh Bachchan, Age: 82
# Name: Priyanka Chopra, Age: 42
# Name: Kareena Kapoor, Age: 44
# Name: Hrithik Roshan, Age: 50
# Name: Ranbir Kapoor, Age: 42
# Name: Vidya Balan, Age: 46
# Name: Anushka Sharma, Age: 36
# Name: Rajinikanth, Age: 74
# Name: Vijay, Age: 50

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Ensures the data structure is a list of dictionaries.
- Uses a generator to iterate efficiently over employees.
- Safely extracts and validates name and age fields.
- Applies an even-number check using modulo (% 2 == 0).
- Converts age to int before checking parity.
- Skips invalid, negative, or malformed records.
- Separates data loading, filtering logic, and output.

# Key Points (Output)
- Prints employee name and age line by line.
- Only employees with even ages are displayed.
- Order follows the JSON file sequence.
- Example output:
  Name: Amitabh Bachchan, Age: 82

# Important Note
- Modulo (%) is the standard way to check even/odd numbers.
- Generators are memory-efficient for large employee datasets.
'''
