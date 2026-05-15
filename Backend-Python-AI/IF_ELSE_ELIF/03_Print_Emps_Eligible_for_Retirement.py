'''
13. Print employees eligible for retirement (age ≥ 60).
'''

import json
from typing import List, Dict, Generator, Tuple, Union


def load_employees(file_path: str) -> List[Dict]:
    '''
    Load the Employee Data
    '''
    try:
        with open(file_path, 'r') as file:
            employees = json.load(file)

        if not isinstance(employees, list):
            raise ValueError("Not a list of dicts")

        return employees

    except FileNotFoundError as err:
        raise FileNotFoundError(f"File not found: {err}") from err

    except json.JSONDecodeError as err:
        raise ValueError("Invalid JSON format") from err


def retirement_eligible_employees(
    employees: List[Dict],
) -> Generator[Tuple[str, Union[int, float]], None, None]:
    '''
    Yield employee name and age if eligible for retirement (age ≥ 60)
    '''
    for employee in employees:
        if not isinstance(employee, dict):
            continue

        name = employee.get("ename")
        age = employee.get("age")

        # Type + domain validation
        if not isinstance(name, str) or not isinstance(age, (int, float)):
            continue
        if not name or age < 0:
            continue

        if age >= 60:
            yield name, age


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name, age in retirement_eligible_employees(employees):
            print(f"Name: {name}, Age: {age} (Eligible for Retirement)")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Name: Amitabh Bachchan, Age: 82 (Eligible for Retirement)
# Name: Rajinikanth, Age: 74 (Eligible for Retirement)

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Confirms the data is a list of dictionaries.
- Uses a generator to process employees efficiently.
- Safely extracts and validates name and age fields.
- Applies a clear condition (age ≥ 60) for retirement eligibility.
- Skips invalid or malformed employee records.
- Separates data loading, filtering logic, and output.

# Key Points (Output)
- Prints employee name and age for eligible employees.
- Only employees aged 60 or above are displayed.
- Output order follows the JSON file sequence.
- Example output:
  Name: Amitabh Bachchan, Age: 82 (Eligible for Retirement)

# Important Note
- Generators are suitable for large datasets.
- Clear conditions make eligibility rules easy to modify later.
'''
