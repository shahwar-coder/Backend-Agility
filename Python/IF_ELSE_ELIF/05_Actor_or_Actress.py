'''
15. Print employee name with label “Actor” if Male else “Actress”.
'''

import json
from typing import List, Dict, Generator, Tuple


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


def actor_or_actress(
    employees: List[Dict],
) -> Generator[Tuple[str, str], None, None]:
    for employee in employees:

        # Type validation
        if not isinstance(employee, dict):
            continue

        name = employee.get("ename")
        gender = employee.get("gender")

        if not isinstance(name, str) or not isinstance(gender, str):
            continue

        # Domain validation
        if not name or gender.lower() not in ("male", "female"):
            continue

        # Business logic
        label = "Actor" if gender.lower() == "male" else "Actress"
        yield name, label


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name, label in actor_or_actress(employees):
            print(f"Name: {name}, Label: {label}")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Name: Shah Rukh Khan, Label: Actor
# Name: Deepika Padukone, Label: Actress
# Name: Amitabh Bachchan, Label: Actor
# Name: Priyanka Chopra, Label: Actress
# Name: Aamir Khan, Label: Actor
# Name: Kareena Kapoor, Label: Actress
# Name: Salman Khan, Label: Actor
# Name: Katrina Kaif, Label: Actress
# Name: Hrithik Roshan, Label: Actor
# Name: Alia Bhatt, Label: Actress
# Name: Akshay Kumar, Label: Actor
# Name: Kangana Ranaut, Label: Actress
# Name: Ranbir Kapoor, Label: Actor
# Name: Vidya Balan, Label: Actress
# Name: Ranveer Singh, Label: Actor
# Name: Anushka Sharma, Label: Actress
# Name: Rajinikanth, Label: Actor
# Name: Aishwarya Rai, Label: Actress
# Name: Vijay, Label: Actor
# Name: Madhuri Dixit, Label: Actress

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Validates that the data is a list of dictionaries.
- Uses a generator to process employees one by one.
- Safely extracts and validates name and gender fields.
- Applies a simple conditional check on gender.
- Labels employees as "Actor" if Male, otherwise "Actress".
- Skips invalid or malformed employee records.
- Separates data loading, labeling logic, and output.

# Key Points (Output)
- Prints employee name with the corresponding label.
- Every valid employee is labeled as Actor or Actress.
- Order follows the JSON file sequence.
- Example output:
  Name: Shah Rukh Khan, Label: Actor

# Important Note
- Case-insensitive gender checks improve robustness.
- Generators are memory-efficient for large datasets.
'''
