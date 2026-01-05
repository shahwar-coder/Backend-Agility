'''
Print employees whose name length is greater than 12 characters.
'''

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


def employees_length_greater_12(
    employees: List[Dict]
) -> Generator[str, None, None]:
    for employee in employees:

        # Type validation
        if not isinstance(employee, dict):
            continue

        name = employee.get("ename")

        if not isinstance(name, str):
            continue

        # Business logic
        if len(name) >= 12:
            yield name


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name in employees_length_greater_12(employees):
            print(f"{name}")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Shah Rukh Khan
# Deepika Padukone
# Amitabh Bachchan
# Priyanka Chopra
# Kareena Kapoor
# Katrina Kaif
# Hrithik Roshan
# Akshay Kumar
# Kangana Ranaut
# Ranbir Kapoor
# Ranveer Singh
# Anushka Sharma
# Aishwarya Rai
# Madhuri Dixit