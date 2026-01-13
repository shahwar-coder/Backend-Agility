'''
3️⃣ Reading Products from Disk

A background job needs to process product data stored locally in products.json.

Question:
Write code to load the JSON file and return the total number of products.
'''

import json

# relevant function written here
def load_file_from_disk(file_path: str):
    '''Load saved file (from disk)'''
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
        
        if not isinstance(data, list):
            raise ValueError("Products not a list")
        
        return len(data)
    
    except FileNotFoundError as err:
        raise FileNotFoundError("Products file not found") from err
    except json.JSONDecodeError as err:
        raise ValueError("Invalid JSON format in products file") from err


def main()->None:
    try:
        total_products = load_file_from_disk(file_path="Python/json/products.json")
        print(f"Total Products : {total_products}")
        
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Total Products : 30

'''
# Key Points (Solution)
- Opens a local JSON file in read mode with UTF-8 encoding.
- Uses json.load() to deserialize JSON into a Python object.
- Validates that the loaded data is a list of products.
- Returns the total number of products using len().
- Handles missing file errors explicitly.
- Handles invalid or corrupted JSON safely.
- Keeps file I/O, validation, and usage logic separated.

# Key Points (Why This Is Backend-Style)
- Defensive checks protect background jobs from bad data.
- Clear error messages simplify debugging and monitoring.
- Returns clean, minimal data for downstream processing.

# Key Points (Output)
- Output is a single integer.
- Represents the total number of products stored on disk.
- Example output:
  Total Products : 30

# Important Note
- json.load() reads directly from a file object.
- Always validate persisted data before processing.
'''
