'''Read this one carefully.
SCENARIO:
A backend developer fetches product data from an external API:
https://dummyjson.com/products

TASK:
After parsing the API JSON response:
- Extract a small subset of fields (id, title, price, category)
- Display the extracted product data using `tabulate`
- Keep the table compact and readable

GOAL:
Practice formatting real API-style JSON responses
into tables for debugging and inspection.
'''

from typing import List, Dict
import requests
from tabulate import tabulate


FIELDS = ("id", "title", "price", "category")


def fetch_products(url: str) -> List[Dict[str, object]]:
    """Fetch product data from external API."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    products = data.get("products")

    if not isinstance(products, list):
        raise ValueError("Invalid API response structure")

    return products


def extract_product_fields(products: List[Dict[str, object]]) -> List[Dict[str, object]]:
    """Extract required fields for display."""
    extracted = []

    for product in products:
        row = {field: product.get(field) for field in FIELDS}
        extracted.append(row)

    return extracted


def display_products(products: List[Dict[str, object]]) -> None:
    """Display products in a compact table."""
    if not products:
        print("No products found")
        return

    print(
        tabulate(
            products,
            headers="keys",
            tablefmt="simple",
            floatfmt=".2f"
        )
    )


def main() -> None:
    try:
        products = fetch_products("https://dummyjson.com/products")
        compact_products = extract_product_fields(products)
        display_products(compact_products)

    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


'''
# Key Points (Solution)
- Fetches real product data from an external API using requests.
- Parses JSON response safely and validates response structure.
- Extracts only a small, relevant subset of fields:
  id, title, price, category.
- Avoids passing full API payloads to the display layer.
- Keeps extraction logic separate from fetching and display logic.

# Key Points (Why Field Extraction Matters)
- API responses are often large and noisy.
- Debugging becomes easier with reduced, focused data.
- Prevents accidental logging of sensitive or unnecessary fields.
- Mirrors real backend practice (DTO / response shaping).

# Key Points (tabulate Usage)
- Uses tabulate to format dictionaries into a readable table.
- headers="keys" automatically maps dict keys to columns.
- tablefmt="simple" keeps output compact and clean.
- floatfmt=".2f" ensures prices are consistently formatted.

# Key Points (Backend Debugging Value)
- Tables are easier to scan than raw JSON.
- Useful for local debugging, logs, and quick inspections.
- Helps verify API contracts and field correctness quickly.
- Commonly used during development, not production responses.

# Key Points (Output Characteristics)
- One row per product.
- Only selected fields are shown.
- Output is human-readable and aligned.
- Example columns:
  id | title | price | category

# Important Note
- This is a debugging/inspection pattern.
- In production, data would typically go to logs,
  monitoring tools, or downstream services instead.
'''
