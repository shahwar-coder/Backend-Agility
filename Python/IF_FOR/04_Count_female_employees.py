'''
4. Count total number of Female employees.
'''

import json
from typing import List, Dict

def load_employees_data(file_path: str)->List[Dict]:
    '''
    Load Json Data
    '''
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("Data loaded is not a list")
            
        return data
        
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found : {file_path}")
        
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON Format")

def total_female_employees(employees: List[Dict])->int:
    '''
    Count total number of Female employees
    '''
    if not employees:
        return 0
    
    females: int = 0
    for employee in employees:
        if not isinstance(employee, dict):
            continue

        gender = employee.get("gender")
        
        if isinstance(gender, str):
            if gender.lower()=="female":
                females+=1
    return females

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        females = total_female_employees(employees)
        print(f"Total female employees: {females}")
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()

# Total female employees: 10

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Verifies that the loaded data is a list of dictionaries.
- Iterates through each employee using a for loop.
- Safely accesses the "gender" field with dict.get().
- Uses case-insensitive comparison to match "female".
- Counts only valid female employee records.
- Skips invalid or malformed entries.
- Returns the total count as an integer.

# Key Points (Output)
- Output is a single integer value.
- Represents the total number of female employees.
- Count is derived from filtered JSON data.
- Example output: 10

# Important Note
- Case-insensitive checks improve reliability.
- Returning a count makes the function reusable and testable.
'''
