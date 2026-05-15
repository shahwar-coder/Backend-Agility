'''
6. Print employee names whose age is less than 40.
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

def print_employees_age_less_40(employees: List[Dict])->None:
    '''
    Print employee names whose age is less than 40.
    '''
    if not employees:
        # print("No employees") # avoid printing inside logic
        return # since no return type, we can simply `return`
    
    for employee in employees:
        if not isinstance(employee, dict):
            continue
        
        age = employee.get("age")
        
        if isinstance(age, int) and age<40:
            name = employee.get("ename")
            
            if name:
                print(name)

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        print_employees_age_less_40(employees)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()

# Deepika Padukone
# Alia Bhatt
# Kangana Ranaut
# Ranveer Singh


'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Confirms the data structure is a list of dictionaries.
- Iterates through employees using a for loop.
- Safely accesses the "age" field via dict.get().
- Filters employees whose age is less than 40.
- Prints names only when a valid name exists.
- Skips invalid or malformed records.
- Keeps logic and error handling separate.

# Key Points (Output)
- Prints employee names line by line.
- Only employees younger than 40 are displayed.
- Order matches the JSON file sequence.
- Example output: Deepika Padukone, Alia Bhatt, etc.

# Important Note
- Strict comparison (< 40) avoids ambiguity.
- Early return keeps the function clean and reusable.
'''
# Anushka Sharma
