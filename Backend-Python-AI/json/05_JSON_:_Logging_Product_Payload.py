'''
4️⃣ Logging Product Payload

A backend service wants to log the product payload before sending it to another service.

Question:
Convert the Python dictionary containing product data into a JSON string suitable for logging.
'''

import json
from typing import Dict, Any


def convert_product_payload_to_json(product: Dict[str, Any]) -> str:
    """Convert product dictionary to JSON string for logging"""
    if not isinstance(product, dict):
        raise ValueError("Product payload must be a dictionary")

    try:
        return json.dumps(product, ensure_ascii=False)
    except (TypeError, ValueError) as err:
        raise ValueError("Product payload is not JSON serializable") from err


def main() -> None:
    try:
        product_payload = {
            "id": 101,
            "name": "Wireless Mouse",
            "price": 799,
            "category": "electronics",
            "in_stock": True
        }

        json_payload = convert_product_payload_to_json(product_payload)
        print(f"Product payload for logging: {json_payload}")

    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

# Output:
# Product payload for logging: {"id": 101, "name": "Wireless Mouse", "price": 799, "category": "electronics", "in_stock": true}


'''
# Key Points (Solution)
- Converts a Python dictionary into a JSON string using json.dumps().
- Validates that the input payload is a dictionary.
- Uses ensure_ascii=False to preserve readable Unicode characters.
- Returns a JSON-formatted string suitable for logs or tracing.
- Handles non-serializable data with clear error handling.
- Keeps conversion logic isolated and reusable.

# Key Points (Why This Is Backend-Style)
- Logging systems expect strings, not Python objects.
- JSON strings are portable across services and languages.
- Defensive checks prevent logging failures in production.

# Key Points (Output)
- Output is a JSON string.
- Represents the product payload in serialized form.
- Boolean values follow JSON standards (true/false).
- Example output:
  {"id": 101, "name": "Wireless Mouse", "price": 799, "category": "electronics", "in_stock": true}

# Important Note
- Use json.dumps() for serialization (dict → string).
- Use json.dump() when writing JSON directly to a file.
'''
