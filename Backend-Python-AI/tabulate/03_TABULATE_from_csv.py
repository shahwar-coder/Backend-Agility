'''
SCENARIO:
A backend job reads a CSV file containing user records
(id, email, status) for manual inspection during debugging.

TASK:
After reading rows from a CSV file:
- Convert the data into a structure suitable for `tabulate`
- Display the rows as a table
- Include headers explicitly

GOAL:
Learn how CSV data is shaped before passing it to `tabulate`.
'''

from typing import List, Dict
from tabulate import tabulate
import csv

REQUIRED_HEADERS = ["id", 'email', 'status'] # using list for deterministic headers is better, using set will bring unstable order for headers

def load_csv(file_path: str)->List[Dict[str, object]]:
    '''Read CSV file of user records....'''
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file) # Produces a structure (List[Dict]) that tabulate loves

            if not reader.fieldnames:
                raise ValueError("CSV file is empty")
            
            if not set(REQUIRED_HEADERS).issubset(reader.fieldnames):
                missing_headers  = set(REQUIRED_HEADERS) - set(reader.fieldnames)
                raise ValueError(f"Headers missing : {missing_headers}")
            
            return list(reader)

    except FileNotFoundError as err:
        raise FileNotFoundError("CSV file of user records not found") from err
    except csv.Error as err:
        raise ValueError("CSV file could not be opened") from err

def display_tabulated_csv(user_records)->None:
    '''Display the CSV data in Table'''
    if not user_records:
        print("No user records found")
        return 
    
    print(
        tabulate(
            user_records,
            headers="keys",
            tablefmt='grid'
        ))

def main()->None:
    try:
        user_records = load_csv("Python/tabulate/user_records.csv")
        display_tabulated_csv(user_records)

    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# +------+-------------------+----------+
# |   id | email             | status   |
# +======+===================+==========+
# |  101 | alice@example.com | active   |
# +------+-------------------+----------+
# |  102 | bob@example.com   | inactive |
# +------+-------------------+----------+
# |  103 | carol@example.com | active   |
# +------+-------------------+----------+
# |  104 | dave@example.com  | pending  |
# +------+-------------------+----------+
# |  105 | eve@example.com   | active   |
# +------+-------------------+----------+


'''
# Key Points (Solution)
- Uses csv.DictReader to read CSV rows as dictionaries.
- Produces a List[Dict], which is the ideal input for tabulate.
- Validates that the CSV file is not empty.
- Ensures required headers (id, email, status) are present.
- Converts CSV rows into a clean, structured Python object.
- Passes the data directly to tabulate for display.

# Key Points (How CSV Data Is Shaped for tabulate)
- Each CSV row becomes one dictionary.
- CSV headers become dictionary keys.
- The list of dictionaries represents table rows.
- headers="keys" tells tabulate to use dict keys as column headers.

# Key Points (Why This Is Backend-Friendly)
- Makes raw CSV data human-readable for debugging.
- Avoids index-based CSV access (more robust).
- Ensures predictable column ordering via REQUIRED_HEADERS.
- Useful for manual inspection, QA, and support workflows.

# Key Points (Output Characteristics)
- Clean grid-style table suitable for terminals.
- Explicit headers: id, email, status.
- One user record per row.
- Easy to scan and verify data integrity.

# Important Note
- csv.DictReader + tabulate is a standard debugging pattern.
- This is meant for inspection, not high-performance pipelines.
- For very large CSVs, streaming rows instead of list()
  would be more memory efficient.
'''
