'''
2. Print employee names whose age is greater than 50.
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

def print_employees_age_greater_50(employees: List[Dict])->None:
    '''
    Print names of all employees whose age > 50
    '''
    if not employees:
        print("No employees in employees data")
        return
    
    for employee in employees:
        if not isinstance(employee, dict):
            continue
        name = employee.get("ename")
        age = employee.get("age")
        
        if isinstance(age, int) and age > 50 and name:
            print(name)

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        print_employees_age_greater_50(employees)
    except Exception as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()

# Shah Rukh Khan
# Amitabh Bachchan
# Aamir Khan
# Salman Khan
# Akshay Kumar
# Rajinikanth
# Aishwarya Rai
# Madhuri Dixit


'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Ensures the data structure is a list of dictionaries.
- Uses a for loop to iterate over all employees.
- Retrieves age and name safely using dict.get().
- Filters employees whose age is greater than 50.
- Prints only valid names with valid integer ages.
- Clean separation of data loading, filtering, and execution.

# Key Points (Output)
- Prints employee names line by line.
- Only employees older than 50 are shown.
- Order matches the JSON file order.
- Example output includes: Shah Rukh Khan, Amitabh Bachchan, etc.

# Important Note
- Type checking (isinstance(age, int)) avoids runtime errors.
- Simple conditional logic is effective for data filtering.
'''

