"""
17. Print employees whose age is an odd number.
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


def employees_with_odd_age(
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
        if int(age) % 2 != 0:
            yield name, age


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name, age in employees_with_odd_age(employees):
            print(f"Name: {name}, Age: {age}")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

# Name: Shah Rukh Khan, Age: 59
# Name: Aamir Khan, Age: 59
# Name: Salman Khan, Age: 59
# Name: Katrina Kaif, Age: 41
# Name: Alia Bhatt, Age: 31
# Name: Akshay Kumar, Age: 57
# Name: Kangana Ranaut, Age: 37
# Name: Ranveer Singh, Age: 39
# Name: Aishwarya Rai, Age: 51
# Name: Madhuri Dixit, Age: 57