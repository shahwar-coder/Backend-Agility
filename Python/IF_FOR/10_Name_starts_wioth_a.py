'''
10. Print employees whose name starts with the letter “A”.
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


def name_starts_with_a(employees: List[Dict]) -> None:
    '''
    Print employees whose name starts with the letter “A”.
    '''
    if not employees:
        return

    for employee in employees:
        if not isinstance(employee, dict):
            continue

        name = employee.get("ename")
        
        if name and isinstance(name, str) and name.lower().startswith("a"):
            print(name)


def main() -> None:
    try:
        employees = load_employees_data("Employee_Data.json")
        name_starts_with_a(employees)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Amitabh Bachchan
# Aamir Khan
# Alia Bhatt
# Akshay Kumar
# Anushka Sharma
# Aishwarya Rai

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Validates that the data is a list of dictionaries.
- Iterates through employees using a for loop.
- Safely accesses the "ename" field with dict.get().
- Uses startswith("a") with lower() for case-insensitive matching.
- Prints only names that begin with the letter "A".
- Skips invalid or malformed records.
- Keeps data loading and processing logic separate.

# Key Points (Output)
- Prints employee names line by line.
- Only employees whose names start with "A" are shown.
- Order follows the JSON file sequence.
- Example output: Amitabh Bachchan, Aamir Khan, Akshay Kumar

# Important Note
- Converting to lowercase ensures consistent matching.
- String methods like startswith() are efficient for prefix checks.
'''
