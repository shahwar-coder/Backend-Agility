'''
7. Print employee names whose age is between 30 and 50.
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

def print_employees_age_between_30_50(employees: List[Dict])->None:
    '''
    Print employee names whose age is between 30 and 50.
    '''
    if not employees:
        # print("No employees") # avoid printing inside logic
        return # since no return type, we can simply `return`
    
    for employee in employees:
        if not isinstance(employee, dict):
            continue
        
        age = employee.get("age")
        name = employee.get("ename")
        
        if isinstance(age, int) and 30 < age < 50 and name:
            print(name)

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        print_employees_age_between_30_50(employees)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")

# Deepika Padukone
# Priyanka Chopra
# Kareena Kapoor
# Katrina Kaif
# Alia Bhatt
# Kangana Ranaut
# Ranbir Kapoor
# Vidya Balan
# Ranveer Singh
# Anushka Sharma

'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Ensures the data is a list of dictionaries.
- Iterates through employees using a for loop.
- Safely retrieves "age" and "ename" using dict.get().
- Applies a chained comparison (30 < age < 50) for clarity.
- Prints only valid employee names within the age range.
- Skips invalid or malformed records.
- Keeps business logic separate from error handling.

# Key Points (Output)
- Prints employee names line by line.
- Only employees aged strictly between 30 and 50 are shown.
- Order follows the JSON file order.
- Example output includes: Deepika Padukone, Priyanka Chopra, etc.

# Important Note
- Chained comparisons are clean and readable in Python.
- Adjust operators (<= / >=) if inclusive bounds are required.
'''
    
if __name__=="__main__":
    main()
