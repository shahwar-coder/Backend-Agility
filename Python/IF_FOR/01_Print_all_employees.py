'''
1. Print all employee names using a for loop.
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

def print_all_employees(employees: List[Dict])->None:
    '''
    Print names of all employees
    '''
    if not employees:
        print("No employees in employees data")
        return
    
    for employee in employees:
        if not isinstance(employee, dict):
            continue
        name = employee.get("ename")
        if name:
            print(name)
        else:
            print("---")

def main()->None:
    try:
        employees = load_employees_data(file_path="Employee_Data.json")
        print_all_employees(employees)
    except Exception as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()

# Shah Rukh Khan
# Deepika Padukone
# Amitabh Bachchan
# Priyanka Chopra
# Aamir Khan
# Kareena Kapoor
# Salman Khan
# Katrina Kaif
# Hrithik Roshan
# Alia Bhatt
# Akshay Kumar
# Kangana Ranaut
# Ranbir Kapoor
# Vidya Balan
# Ranveer Singh
# Anushka Sharma
# Rajinikanth
# Aishwarya Rai
# Vijay
# Madhuri Dixit
