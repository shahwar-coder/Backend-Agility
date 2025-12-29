'''
Print employee name and age if the employee is Male.
'''

import json
from typing import List, Dict


def load_employees_data(file_path: str) -> List[Dict]:
    '''
    Load JSON employee data
    '''
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Data loaded is not a list")

        return data

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")


def print_male_employee_name_age(employees: List[Dict]) -> None:
    '''
    Print employee name and age if the employee is Male.
    '''
    if not employees:
        return

    for employee in employees:
        if not isinstance(employee, dict):
            continue

        gender = employee.get("gender")

        if isinstance(gender, str) and gender.lower() == "male":
            name = employee.get("ename")
            age = employee.get("age")

            if name and isinstance(age, int):
                print(f"Name: {name}, Age: {age}")


def main() -> None:
    try:
        employees = load_employees_data("Employee_Data.json")
        print_male_employee_name_age(employees)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

# Name: Shah Rukh Khan, Age: 59
# Name: Amitabh Bachchan, Age: 82
# Name: Aamir Khan, Age: 59
# Name: Salman Khan, Age: 59
# Name: Hrithik Roshan, Age: 50
# Name: Akshay Kumar, Age: 57
# Name: Ranbir Kapoor, Age: 42
# Name: Ranveer Singh, Age: 39
# Name: Rajinikanth, Age: 74
# Name: Vijay, Age: 50


'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Ensures the loaded data is a list of dictionaries.
- Iterates through each employee using a for loop.
- Safely accesses "gender", "ename", and "age" using dict.get().
- Uses a case-insensitive check to identify Male employees.
- Prints name and age together in a clean formatted string.
- Skips invalid or malformed employee records.
- Separates data loading, processing, and error handling.

# Key Points (Output)
- Prints employee name and age line by line.
- Only Male employees are displayed.
- Order follows the sequence in the JSON file.
- Example output: Name: Shah Rukh Khan, Age: 59

# Important Note
- Type checking for age ensures reliable output.
- This pattern can be reused for other attribute-based filters.
'''
