'''
SCENARIO:
A backend integrates with an external API that returns data in
multiple pages. Each page contains a list of items.

TASK:
Write a generator function `iterate_items(pages)` that:
- Accepts a list of pages (each page is a list)
- Yields items one by one across all pages
- Does not combine pages into a single list
'''

from typing import Iterable, Generator, Any, Dict


def iterate_items(pages: Iterable[Iterable[Dict[str, Any]]]) -> Generator[Dict[str, Any], None, None]:
    """
    Stream items across paginated API responses.

    - Accepts an iterable of pages
    - Each page is an iterable of items
    - Yields items one by one without combining pages
    """
    if pages is None:
        raise ValueError("Pages source cannot be None")

    for page in pages:
        # Defensive: skip invalid or empty pages
        if not isinstance(page, Iterable):
            continue

        for item in page:
            # Defensive: ensure item is a dictionary (API contract)
            if isinstance(item, dict):
                yield item


def main() -> None:
    pages = [
        [
            {"id": 1, "name": "Laptop", "price": 75000},
            {"id": 2, "name": "Mouse", "price": 1200},
            {"id": 3, "name": "Keyboard", "price": 2500},
        ],
        [
            {"id": 4, "name": "Monitor", "price": 18000},
            {"id": 5, "name": "USB Hub", "price": 2200},
        ],
        [
            {"id": 6, "name": "Webcam", "price": 3500},
            {"id": 7, "name": "Headphones", "price": 4200},
            {"id": 8, "name": "Microphone", "price": 5600},
        ],
    ]

    try:
        for item in iterate_items(pages):
            print(item)
    except Exception as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

# - This solution is optimized because each item is processed exactly once.
# - Nested loops here do NOT mean O(n²); complexity is O(N), where N = total items.
# - Pages are partitions of input, not a second dimension of work.
# - No page or item list is flattened → no extra memory usage.
# - Generator enforces sequential consumption and prevents accidental duplication.
# - Accepts Iterable instead of List → works with APIs, DB cursors, streams.
# - Defensive checks are minimal and realistic (skip bad data, fail on bad boundary).
# - Optimization here means avoiding unnecessary work, not clever tricks.
# - This is the same pattern used for API pagination and database cursors.

'''
IMPORTANT : If each record is visited once, total work is linear — regardless of how many loops exist.
'''

# {'id': 1, 'name': 'Laptop', 'price': 75000}
# {'id': 2, 'name': 'Mouse', 'price': 1200}
# {'id': 3, 'name': 'Keyboard', 'price': 2500}
# {'id': 4, 'name': 'Monitor', 'price': 18000}
# {'id': 5, 'name': 'USB Hub', 'price': 2200}
# {'id': 6, 'name': 'Webcam', 'price': 3500}
# {'id': 7, 'name': 'Headphones', 'price': 4200}
# {'id': 8, 'name': 'Microphone', 'price': 5600}


'''
# Key Points (Solution)
- Uses a generator to stream items across paginated responses.
- Accepts any Iterable of pages (not limited to lists).
- Each page is processed sequentially, one at a time.
- Items are yielded one by one without flattening pages.
- Avoids building intermediate lists → memory efficient.
- Defensive checks skip invalid pages and non-dict items.
- Enforces API contract by yielding only dictionary items.
- Raises error only for invalid top-level input (pages=None).

# Key Points (Why This Is Backend-Style)
- Mirrors real-world API pagination and DB cursor patterns.
- Works with large datasets and streaming sources.
- Prevents accidental duplication or eager loading.
- Safe to plug into pipelines, processors, or writers.
- Iterable-based design increases reusability and flexibility.

# Key Points (Complexity & Performance)
- Time complexity is O(N), where N = total items across all pages.
- Nested loops do NOT imply O(n²) here.
- Each record is visited exactly once.
- No extra memory usage for combining or copying data.

# Key Points (Output Behavior)
- Items are yielded in page order, then item order.
- Consumer controls how much data is processed.
- Example output: one product dict printed at a time.

# Important Note
- Number of loops ≠ time complexity.
- If total work scales with total items, it is linear.
- This exact pattern is used in production pagination systems.
'''
