'''
Question 2 — Writing Processed Data to CSV (Export / Reporting)

You have a list of dictionaries representing product data:
products = [
    {"id": 101, "name": "Laptop", "price": 75000},
    {"id": 102, "name": "Phone", "price": 40000}
]

Write code that:
- Writes this data to a CSV file using the csv module
- Ensures column order is consistent
- Writes headers explicitly
- Produces a CSV that can be safely shared with other services or teams

Focus on:
Correct writer choice
Predictable output structure
'''

import csv
from typing import List, Dict

def write_products_to_csv(products: List[Dict[str, object]], file_path: str) -> None:
    """
    Write product data to a CSV file in a predictable, shareable format.
    """
    if not products:
        raise ValueError("No products provided to write")

    # Explicit, consistent column order
    fieldnames = ["id", "name", "price"]

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write headers explicitly
            writer.writeheader()

            # Write rows
            for product in products:
                writer.writerow(product)

    except OSError as err:
        raise OSError("Failed to write products CSV file") from err


def main() -> None:
    products = [
        {"id": 101, "name": "Laptop", "price": 75000},
        {"id": 102, "name": "Phone", "price": 40000},
    ]

    try:
        write_products_to_csv(products, "Python/csv/products_writing.csv")
        print("Products CSV written successfully.")
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


'''This is the crux for me while solving the problem
# WRITE HEADERS EXPLICILY
writer.writeheader()

# WRITE ROWS
for product in products:
    writer.writerow(product)
'''
# ============
'''READER VS WRITER
reader = csv.DictReader
writer = csv.DictWriter
'''

# Output:
# Products CSV written successfully.

'''
# Key Points (Solution)
- Uses csv.DictWriter to write dictionaries directly to CSV.
- Defines explicit fieldnames to guarantee column order.
- Writes headers using writer.writeheader().
- Opens file with newline="" so csv module controls line endings.
- Uses UTF-8 encoding for safe cross-system compatibility.
- Iterates over product dictionaries and writes each row.
- Produces a clean, predictable CSV structure.

# Key Points (Why This Is Backend-Style)
- Explicit schema prevents breaking downstream consumers.
- DictWriter avoids positional errors common with csv.writer.
- Header inclusion makes files self-describing.
- Predictable column order is essential for imports, analytics, and ETL.
- CSV output is portable across services, languages, and tools.

# Key Points (Output)
- Creates a CSV file with columns: id, name, price.
- Each product is written as one row.
- File is safe to share with other teams or systems.
- Example CSV content:
  id,name,price
  101,Laptop,75000
  102,Phone,40000

# Important Note
- Always control fieldnames when exporting CSVs.
- This pattern is standard for reporting and data exchange in backends.
'''
