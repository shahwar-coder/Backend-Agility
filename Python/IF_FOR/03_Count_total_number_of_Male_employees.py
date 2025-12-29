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
        name = employee.get("ename")
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

# Poutput: 10

'''
# Key Points (Solution)
- Loads employee records from a JSON file.
- Ensures the loaded data is a list of dictionaries.
- Iterates through employees using a for loop.
- Safely reads the "gender" field using dict.get().
- Converts gender to lowercase for case-insensitive comparison.
- Counts entries where gender == "male".
- Ignores invalid or malformed employee records.
- Returns the total count as an integer.

# Key Points (Output)
- Output is a single integer value.
- Represents the total number of male employees.
- Correctly reflects filtered data from the JSON file.
- Example output: 10

# Important Note
- Case-insensitive checks improve data robustness.
- Returning a count makes the function reusable in other logic.
'''
