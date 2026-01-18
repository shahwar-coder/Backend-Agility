"""Read this
SCENARIO:
A backend tool is used by developers and analysts,
each preferring a different table format.

TASK:
- Display the same dataset using THREE tabulate formats
- Keep underlying data unchanged
"""

from typing import List, Dict
from tabulate import tabulate


products: List[Dict[str, object]] = [
    {"id": 1, "title": "Laptop", "price": 75000, "category": "electronics"},
    {"id": 2, "title": "Smartphone", "price": 32000, "category": "electronics"},
    {"id": 3, "title": "Headphones", "price": 2500, "category": "accessories"},
]


def display_in_multiple_formats(data: List[Dict[str, object]]) -> None:
    """Display the same data using different tabulate formats."""
    if not data:
        print("No data to display")
        return

    formats = {
        "PLAIN": "plain",
        "GRID": "grid",
        "GITHUB": "github",
    }

    for name, fmt in formats.items():
        print(f"\n{name} FORMAT")
        print("-" * 40)
        print(tabulate(data, headers="keys", tablefmt=fmt))


def main() -> None:
    try:
        display_in_multiple_formats(products)
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()


# PLAIN FORMAT
# ----------------------------------------
#   id  title         price  category
#    1  Laptop        75000  electronics
#    2  Smartphone    32000  electronics
#    3  Headphones     2500  accessories

# GRID FORMAT
# ----------------------------------------
# +------+------------+---------+-------------+
# |   id | title      |   price | category    |
# +======+============+=========+=============+
# |    1 | Laptop     |   75000 | electronics |
# +------+------------+---------+-------------+
# |    2 | Smartphone |   32000 | electronics |
# +------+------------+---------+-------------+
# |    3 | Headphones |    2500 | accessories |
# +------+------------+---------+-------------+

# GITHUB FORMAT
# ----------------------------------------
# |   id | title      |   price | category    |
# |------|------------|---------|-------------|
# |    1 | Laptop     |   75000 | electronics |
# |    2 | Smartphone |   32000 | electronics |
# |    3 | Headphones |    2500 | accessories |

'''
# Key Points (Solution)
- Uses the same underlying dataset without modification.
- Demonstrates multiple tabulate formats from a single data source.
- Formats shown: plain, grid, github.
- headers="keys" ensures dictionary keys are used as column headers.
- Clean separation between data and presentation.

# Key Points (Why This Is Backend-Friendly)
- Different teams prefer different table styles.
- Same data can be reused across CLI tools and reports.
- Avoids duplicating or transforming data for display.
- Makes debugging and inspection more flexible.

# Key Points (Format Use Cases)
- plain   → quick scans, minimal noise, logs
- grid    → human-friendly, terminal inspection
- github  → markdown-ready, documentation and PRs

# Key Points (Design Principle)
- Data stays constant, only presentation changes.
- Presentation layer should be swappable.
- Encourages clean, reusable backend utilities.

# Important Note
- tabulate supports many formats (psql, fancy_grid, rst, etc.).
- Choosing format depends on audience, not data.
'''
