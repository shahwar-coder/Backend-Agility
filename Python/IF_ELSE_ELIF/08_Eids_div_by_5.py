'''Print employees with eid divisible by 5.'''

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


def employees__age_div_by_5(
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
        if int(age) % 5 == 0:
            yield name, age


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name, age in employees__age_div_by_5(employees):
            print(f"Name: {name}, Age: {age}")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Name: Hrithik Roshan, Age: 50
# Name: Vijay, Age: 50