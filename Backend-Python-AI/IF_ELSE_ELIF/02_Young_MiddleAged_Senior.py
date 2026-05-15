'''
12. Print “Young”, “Middle-aged”, or “Senior” based on age:
< 40   → Young
40–59  → Middle-aged
>= 60  → Senior
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


def classify_employee_by_age(
    employees: List[Dict],
) -> Generator[Tuple[str, Union[int, float], str], None, None]:
    '''
    Yield Name, Age, and Age Category (Young / Middle-aged / Senior)
    '''
    for employee in employees:
        if not isinstance(employee, dict):
            raise ValueError("Employee details not dict")

        name = employee.get("ename")
        age = employee.get("age")

        # Type validation
        if not isinstance(name, str) or not isinstance(age, (int, float)):
            continue

        # Domain validation
        if not name or age < 0:
            continue

        # Classification logic
        if age < 40:
            category = "Young"
        elif 40 <= age <= 59:
            category = "Middle-aged"
        else:
            category = "Senior"

        yield name, age, category


def main() -> None:
    try:
        employees = load_employees("IF_ELSE_ELIF/Employee_Data.json")
        for name, age, category in classify_employee_by_age(employees):
            print(f"Name: {name}, Age: {age}, Category: {category}")

    except (ValueError, FileNotFoundError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Name: Shah Rukh Khan, Age: 59, Category: Middle-aged
# Name: Deepika Padukone, Age: 38, Category: Young
# Name: Amitabh Bachchan, Age: 82, Category: Senior
# Name: Priyanka Chopra, Age: 42, Category: Middle-aged
# Name: Aamir Khan, Age: 59, Category: Middle-aged
# Name: Kareena Kapoor, Age: 44, Category: Middle-aged
# Name: Salman Khan, Age: 59, Category: Middle-aged
# Name: Katrina Kaif, Age: 41, Category: Middle-aged
# Name: Hrithik Roshan, Age: 50, Category: Middle-aged
# Name: Alia Bhatt, Age: 31, Category: Young
# Name: Akshay Kumar, Age: 57, Category: Middle-aged
# Name: Kangana Ranaut, Age: 37, Category: Young
# Name: Ranbir Kapoor, Age: 42, Category: Middle-aged
# Name: Vidya Balan, Age: 46, Category: Middle-aged
# Name: Ranveer Singh, Age: 39, Category: Young
# Name: Anushka Sharma, Age: 36, Category: Young
# Name: Rajinikanth, Age: 74, Category: Senior
# Name: Aishwarya Rai, Age: 51, Category: Middle-aged
# Name: Vijay, Age: 50, Category: Middle-aged
# Name: Madhuri Dixit, Age: 57, Category: Middle-aged


'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Ensures the data is a list of dictionaries.
- Uses a generator to classify employees one by one.
- Safely extracts and validates name and age fields.
- Applies clear if–elif–else logic for age classification.
- Categories:
  - Age < 40  → Young
  - Age 40–59 → Middle-aged
  - Age ≥ 60  → Senior
- Skips invalid or malformed employee records.
- Separates data loading, classification logic, and output.

# Key Points (Output)
- Prints employee name, age, and age category.
- Each employee is labeled as Young, Middle-aged, or Senior.
- Output order matches the JSON file sequence.
- Example output:
  Name: Amitabh Bachchan, Age: 82, Category: Senior

# Important Note
- Generators are memory-efficient for large datasets.
- Explicit ranges make the classification logic easy to read and maintain.
'''
