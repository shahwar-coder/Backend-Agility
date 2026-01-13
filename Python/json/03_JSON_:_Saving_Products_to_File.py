'''
2️⃣ Saving Products to File

The products API response has already been converted into a Python dictionary.

Question:
Write code to store this products data into a file named products.json.
'''

import requests
import json
from typing import List, Dict

def fetch_products(url: str)-> List[Dict]:
    """Fetch Products"""
    try:
        # call api
        response = requests.get(url) # gives you response object != json string
        response.raise_for_status() # http error handling

        # response object as python object
        data = response.json() # directly we have option to get python object here,--- # no need for indirect -> "json.loads(response.text)"

        # validate `data`/response structure
        if not isinstance(data, dict):
            raise ValueError("Invalid response format")
        
        # concerned values `products`
        products = data.get("products")

        if not isinstance(products, list):
            raise ValueError("Products key missing or invalid")
        
        return products
        
    except requests.exceptions.RequestException as err:
        raise RuntimeError(f"API request failed: {err}")
    
    except json.JSONDecodeError as err:
        raise ValueError("Invalid JSON response") from err
    
def save_products_to_file(products: List[Dict], file_path):
    '''Save products to a file'''
    if not isinstance(products, list):
        raise ValueError("Products must be a list")
    try:
        with open(file_path, 'w', encoding="utf-8") as file: # encoding for things like `name = "मोबाइल"` etc.
            json.dump(products, file, indent=2) 
    except OSError as err: # FileNotFoundError, json.JSONDecodeError can NOT be used here in exceptions with dump() 
        raise OSError("Failed to write products in file") from err


def main()->None:
    try:
        products = fetch_products("https://dummyjson.com/products")
        save_products_to_file(products, "Python/json/products.json")
        print("Products saved successfully!")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Products saved successfully!

'''
# Key Points (Solution)
- Fetches products from an external API and converts them to Python objects.
- Validates that products data is a list of dictionaries.
- Opens a file in write mode with UTF-8 encoding.
- Uses json.dump() to serialize Python objects into JSON format.
- Applies indent=2 for readable, pretty-printed JSON.
- Handles file system errors using OSError.
- Keeps fetching, saving, and execution logic clearly separated.

# Key Points (Why This Is Backend-Style)
- Ensures data validation before persistence.
- Uses explicit encoding for international characters.
- Writes structured, readable JSON suitable for logs or storage.
- Handles I/O errors gracefully.

# Key Points (Output)
- Creates a file named products.json at the given path.
- File contains a JSON array of product objects.
- Confirms success with a clear message:
  "Products saved successfully!"

# Important Note
- json.dump() writes directly to a file (no intermediate string).
- Always validate external data before storing it.
'''
