'''
SCENARIO:
A backend service loads configuration data from a JSON file
containing environment details for multiple services.

TASK:
Given a list of dictionaries loaded from JSON:
- Use `tabulate` to display the data as a clean table
- Show keys as column headers
- Ensure the output is readable in a terminal

GOAL:
Understand how `tabulate` works with JSON-style
(list of dict) data structures.
'''

from typing import List, Dict
from tabulate import tabulate
import json

def load_json(file_path: str)->List[Dict[str, object]]:
    '''Load JSON file'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("Config Data Should be a List")
        
        return data
    
    except FileNotFoundError as err:
        raise FileNotFoundError("Configuration file not found") from err
    
    except json.JSONDecodeError as err:
        raise ValueError("Invalid JSON format in configuration file") from err

def display_tabulated_json(config_data: List[Dict[str, object]])->None:
    '''Display configuration data in a clean table format'''
    if not config_data:
        print("No configuration entries found")
        return
    print(
        tabulate(
        config_data, 
        headers='keys',
        tablefmt='grid'))

def main()->None:
    try:
        config_data = load_json("Python/tabulate/config_data.json")
        display_tabulated_json(config_data)

    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()


# Output:
# +----------------------+---------------+-----------------------+--------+---------+
# | service              | environment   | host                  |   port | debug   |
# +======================+===============+=======================+========+=========+
# | auth-service         | production    | auth.prod.internal    |    443 | False   |
# +----------------------+---------------+-----------------------+--------+---------+
# | user-service         | staging       | user.staging.internal |   8080 | True    |
# +----------------------+---------------+-----------------------+--------+---------+
# | payment-service      | production    | pay.prod.internal     |    443 | False   |
# +----------------------+---------------+-----------------------+--------+---------+
# | notification-service | development   | localhost             |   5000 | True    |
# +----------------------+---------------+-----------------------+--------+---------+


'''
# Key Points (Solution)
- Loads configuration data from a JSON file into Python objects.
- Ensures the JSON structure is a list of dictionaries.
- Uses tabulate to render list-of-dict data directly as a table.
- headers="keys" automatically maps dictionary keys to column headers.
- tablefmt="grid" produces a clear, terminal-friendly table layout.
- Handles empty configuration gracefully.

# Key Points (How tabulate Works with JSON-style Data)
- Each dictionary represents one row.
- Dictionary keys become column names.
- Values are aligned under their respective headers.
- Order of columns follows key order in dictionaries.

# Key Points (Why This Is Backend-Friendly)
- Makes configuration and environment data easy to inspect.
- Ideal for debugging deployments and service configs.
- Much more readable than raw JSON in logs or terminals.
- Helps quickly verify environment-specific settings.
- Commonly used in ops tools, admin CLIs, and diagnostics.

# Key Points (Output Characteristics)
- Clean, aligned table suitable for terminals.
- One service per row.
- Columns such as service, environment, host, port, debug.
- Readable even for non-developers (ops / support teams).

# Important Note
- tabulate is for human inspection, not machine output.
- In production systems, this is typically used in:
  - CLI tools
  - Debug scripts
  - Admin dashboards
'''
