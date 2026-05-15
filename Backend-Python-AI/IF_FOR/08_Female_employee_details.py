'''
8. Print employee name and age if the employee is Female.
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

def print_female_employee_name_age(employees: List[Dict])->None:
    '''
    8. Print employee name and age if the employee is Female.
    '''
    if not employees:
        # print("No employees") # avoid printing inside logic
        return # since no return type, we can simply `return`
    
    for employee in employees:
        if not isinstance(employee, dict):
            continue
        
        gender = employee.get("gender")
        
        if isinstance(gender, str) and gender.lower()=="female":
            age = employee.get("age")
            name = employee.get("ename")
            if age and name: # more checks can be put here
                print(f"Name: {name}, Age: {age}") 
        

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        print_female_employee_name_age(employees)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")


if __name__=="__main__":
    main()


# Name: Deepika Padukone, Age: 38
# Name: Priyanka Chopra, Age: 42
# Name: Kareena Kapoor, Age: 44
# Name: Katrina Kaif, Age: 41
# Name: Alia Bhatt, Age: 31
# Name: Kangana Ranaut, Age: 37
# Name: Vidya Balan, Age: 46
# Name: Anushka Sharma, Age: 36
# Name: Aishwarya Rai, Age: 51
# Name: Madhuri Dixit, Age: 57


'''
# Key Points (Solution)
- Loads employee data from a JSON file.
- Confirms the data is a list of dictionaries.
- Iterates through employees using a for loop.
- Safely reads "gender", "ename", and "age" using dict.get().
- Uses case-insensitive check to identify Female employees.
- Prints both name and age together in a formatted output.
- Skips invalid or malformed records.
- Keeps logic separate from file handling and error handling.

# Key Points (Output)
- Prints employee name and age per line.
- Only Female employees are displayed.
- Output order matches the JSON file sequence.
- Example output: Name: Deepika Padukone, Age: 38

# Important Note
- Combining multiple fields in output improves readability.
- Additional type checks can be added for stricter validation.
'''

