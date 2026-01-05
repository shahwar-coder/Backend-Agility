'''
Print employees whose age ends with digit 7 or 9.
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


def employees_age_7_9_in_end(
    employees: List[Dict]
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
        if age%10 == 7 or age%10 == 9:
            yield name, age


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name, age in employees_age_7_9_in_end(employees):
            print(f"{name} : {age}")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Shah Rukh Khan : 59
# Aamir Khan : 59
# Salman Khan : 59
# Akshay Kumar : 57
# Kangana Ranaut : 37
# Ranveer Singh : 39
# Madhuri Dixit : 57