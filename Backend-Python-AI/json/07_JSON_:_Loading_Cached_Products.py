'''
6️⃣ Loading Cached Products

Before calling the external API, the service checks for cached data.

Question:
Write code to load product data from products_cache.json into a Python object.
'''

import json
from typing import List, Dict, Any


def load_products_from_cache(file_path: str) -> List[Dict[str, Any]]:
    """Load cached products from disk into a Python object"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Cached products data is not a list")

        return data

    except FileNotFoundError as err:
        raise FileNotFoundError("Cache file not found") from err

    except json.JSONDecodeError as err:
        raise ValueError("Invalid JSON format in cache file") from err


def main() -> None:
    try:
        products = load_products_from_cache("Python/json/products_cache.json")
        print(f"Loaded {len(products)} products from cache")
        print("Sample product:", products[0] if products else "Cache is empty")
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# Loaded 3 products from cache
# Sample product: {'id': 1, 'name': 'Laptop', 'price': 75000, 'category': 'electronics', 'in_stock': True}


'''
# Key Points (Solution)
- Opens the cached JSON file using UTF-8 encoding.
- Uses json.load() to deserialize JSON into a Python object.
- Validates that cached data is a list of product dictionaries.
- Returns structured Python data for immediate reuse.
- Handles missing cache file and invalid JSON safely.
- Keeps cache-loading logic isolated from API logic.

# Key Points (Why Cache Files Are Useful in Backend Systems)
- Reduces repeated external API calls.
- Improves response time and overall performance.
- Protects systems from API rate limits or downtime.
- Enables graceful fallback when external services fail.
- Useful for background jobs, warm starts, and retries.
- Helps lower infrastructure and network costs.

# Key Points (Output)
- Output is a Python list of product dictionaries.
- Length indicates how many products are cached.
- Can safely access product fields after loading.
- Example output:
  Loaded 3 products from cache
  Sample product: {'id': 1, 'name': 'Laptop', ...}

# Important Note
- Cache files are commonly paired with expiry logic (TTL).
- In production, cache may live in Redis, DB, or filesystem.
'''
