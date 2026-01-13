'''
5️⃣ Caching Products API Response

To reduce API calls, the products API response is cached on disk.

Question:
Write code to save the fetched products data into products_cache.json.
'''

import json
from typing import List, Dict, Any


def save_products_to_cache(products: List[Dict[str, Any]], file_path: str) -> None:
    """Save products data into cache file"""
    if not isinstance(products, list):
        raise ValueError("Products data must be a list")

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(products, file, indent=2, ensure_ascii=False)
    except OSError as err:
        raise OSError("Failed to write products cache file") from err
    # always remember, you cannot get JSON decode error or File not found error while writing to a file.


def main() -> None:
    try:
        # Given products data
        products = [
            {
                "id": 1,
                "name": "Laptop",
                "price": 75000,
                "category": "electronics",
                "in_stock": True
            },
            {
                "id": 2,
                "name": "Smartphone",
                "price": 32000,
                "category": "electronics",
                "in_stock": True
            },
            {
                "id": 3,
                "name": "Headphones",
                "price": 2500,
                "category": "accessories",
                "in_stock": False
            }
        ]

        save_products_to_cache(products, "Python/json/products_cache.json")
        print("Products cached successfully")

    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

# Products cached successfully

'''
# Key Points (Solution)
- Accepts already-fetched products data as a Python list.
- Validates that the products input is a list before caching.
- Opens the cache file in write mode with UTF-8 encoding.
- Uses json.dump() to serialize Python objects directly to disk.
- indent=2 improves readability for debugging and inspections.
- ensure_ascii=False preserves non-ASCII characters.
- Handles file system errors using OSError.
- Keeps caching logic separate from fetching logic.

# Key Points (Why This Is Important in Backend Systems)
- Reduces repeated calls to external APIs.
- Improves response time for subsequent requests.
- Acts as a fallback when external APIs are slow or unavailable.
- Helps avoid API rate limits and throttling.
- Enables faster startup for background jobs and services.
- File-based caching is simple and effective for small-scale systems.

# Key Points (Output)
- Creates/overwrites products_cache.json on disk.
- File contains a JSON array of product objects.
- Confirms success with a clear log message:
  "Products cached successfully"

# Important Note
- json.dump() writes Python objects → JSON file.
- JSONDecodeError cannot occur during writing (only during reading).
- In production, file cache is often replaced by Redis or databases.
'''
