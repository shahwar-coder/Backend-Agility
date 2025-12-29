'''
5. Print employees whose age is exactly 59.
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

def print_employees_age_59(employees: List[Dict])->None:
    '''
    Print employees whose age is exactly 59.
    '''
    if not employees:
        # print("No employees") # avoid printing inside logic
        return # since no return tyoe, we can simply `return`
    
    for employee in employees:
        if not isinstance(employee, dict):
            continue
        
        age = employee.get("age")
        
        if isinstance(age, int) and age==59:
            name = employee.get("ename")
            
            if name:
                print(name)

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        print_employees_age_59(employees)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()


# Shah Rukh Khan
# Aamir Khan
# Salman Khan

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Ensures the data is a list of dictionaries.
- Iterates through employees using a for loop.
- Safely retrieves the "age" field with dict.get().
- Filters employees whose age is exactly 59.
- Prints the employee name only if it exists.
- Skips invalid or malformed records.
- Keeps business logic separate from error handling.

# Key Points (Output)
- Prints employee names line by line.
- Only employees aged exactly 59 are shown.
- Order follows the JSON file sequence.
- Example output: Shah Rukh Khan, Aamir Khan, Salman Khan

# Important Note
- Exact equality (==) is used instead of range checks.
- Avoiding prints inside logic improves reusability.
'''
