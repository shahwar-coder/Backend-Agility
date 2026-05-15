'''
3. Count total number of Male employees
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

def total_male_employees(employees: List[Dict])->int:
    '''
    Count total number of Male employees
    '''
    if not employees:
        return 0
    
    males: int = 0
    for employee in employees:
        if not isinstance(employee, dict):
            continue

        gender = employee.get("gender")
        
        if isinstance(gender, str):
            if gender.lower()=="male":
                males+=1
    return males

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        males = total_male_employees(employees)
        print(f"Total male employees: {males}")
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()

# Total male employees: 10

'''
# Key Points (Solution)
- Loads employee records from a JSON file.
- Confirms the data structure is a list of dictionaries.
- Iterates through employees using a for loop.
- Safely accesses the "gender" field via dict.get().
- Performs case-insensitive comparison for "male".
- Counts only valid male employee entries.
- Ignores malformed or non-dictionary records.
- Returns the total count as an integer.

# Key Points (Output)
- Output is a single integer.
- Represents the total number of male employees.
- Derived from filtering the JSON dataset.
- Example output: 10

# Important Note
- Case-insensitive checks make the logic robust.
- Returning a value allows reuse in reports or analytics.
'''

