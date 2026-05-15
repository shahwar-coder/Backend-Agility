'''
For each employee, print “Senior Employee” if age ≥ 60 
else “Regular Employee”.
'''

import json
from typing import List, Dict, Generator, Tuple, Union

def load_employees(file_path: str)->List[Dict]:
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
        # raise json.JSONDecodeError(f"Json Decode Erorr: {err}") # never re raise Json Decode error
    
def senior_or_regular_employee(employees: List[Dict])->Generator[Tuple[str, Union[int, float], str], None, None]:
    '''
    Yield, Name, Age, Senior or Regular Employee
    '''
    for employee in employees:
        # if not employee: # Checking for emptiness is not required if is instance is used for type checking. (important)
        #     continue

        if not isinstance(employee, dict):
            raise ValueError("Employee details not dict")
        
        name = employee.get("ename")
        age = employee.get("age")

        if not isinstance(name, str) or not isinstance(age, (int, float)): # isinstance(age, Union[int, float]) : INVALID , use tuple instead for multiple data types check.
            continue # we can choose to raise error too

        if not name or age<=0:
            continue # we could raise error too

        status = "Senior Employee" if age >= 60 else "Regular Employee"

        yield name, age, status

def main()->None:
    try:
        employees = load_employees('IF_ELSE_ELIF/Employee_Data.json')
        for name, age, status in senior_or_regular_employee(employees):
            print(f"Name: {name} , Age: {age}, Status: {status}")
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()


# Name: Shah Rukh Khan , Age: 59, Status: Regular Employee
# Name: Deepika Padukone , Age: 38, Status: Regular Employee
# Name: Amitabh Bachchan , Age: 82, Status: Senior Employee
# Name: Priyanka Chopra , Age: 42, Status: Regular Employee
# Name: Aamir Khan , Age: 59, Status: Regular Employee
# Name: Kareena Kapoor , Age: 44, Status: Regular Employee
# Name: Salman Khan , Age: 59, Status: Regular Employee
# Name: Katrina Kaif , Age: 41, Status: Regular Employee
# Name: Hrithik Roshan , Age: 50, Status: Regular Employee
# Name: Alia Bhatt , Age: 31, Status: Regular Employee
# Name: Akshay Kumar , Age: 57, Status: Regular Employee
# Name: Kangana Ranaut , Age: 37, Status: Regular Employee
# Name: Ranbir Kapoor , Age: 42, Status: Regular Employee
# Name: Vidya Balan , Age: 46, Status: Regular Employee
# Name: Ranveer Singh , Age: 39, Status: Regular Employee
# Name: Anushka Sharma , Age: 36, Status: Regular Employee
# Name: Rajinikanth , Age: 74, Status: Senior Employee
# Name: Aishwarya Rai , Age: 51, Status: Regular Employee
# Name: Vijay , Age: 50, Status: Regular Employee
# Name: Madhuri Dixit , Age: 57, Status: Regular Employee


'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Validates that the loaded data is a list of dictionaries.
- Uses a generator to process employees one by one.
- Safely extracts and validates name and age fields.
- Uses a simple if–else condition to classify employees.
- Marks age ≥ 60 as "Senior Employee", otherwise "Regular Employee".
- Skips invalid or malformed employee records.
- Separates data loading, classification logic, and output.

# Key Points (Output)
- Prints employee name, age, and status.
- Every employee is labeled as Senior or Regular.
- Order follows the JSON file sequence.
- Example output:
  Name: Amitabh Bachchan , Age: 82, Status: Senior Employee

# Important Note
- Generators are memory-efficient for large datasets.
- Clear conditional logic improves readability and maintainability.
'''
