'''
TASK 3: SAFE COMPARISON WITH DIFFERENT TYPES

Write a class `Product` with:
- Attributes: product_id and price
- An __eq__ method that:
  - Returns NotImplemented when compared with a non-Product object
  - Compares values only when the other object is a Product

TEST CASES TO CONSIDER:
- Product == Product → value comparison
- Product == string/int → safe comparison

RULES:
- Use isinstance check
- Do NOT raise errors for invalid comparisons

GOAL:
Learn how __eq__ should behave safely
in real-world codebases.
'''

class Product:
    """Represents a product with an ID and price."""

    def __init__(self, product_id: str, price: float) -> None:
        self.product_id = product_id
        self.price = price

    def __repr__(self) -> str:
        return f"Product(product_id={self.product_id!r}, price={self.price!r})"

    def __eq__(self, other) -> bool:
        # Safe comparison with unrelated types
        if not isinstance(other, Product):
            return NotImplemented

        # Value-based comparison
        return (
            self.product_id == other.product_id
            and self.price == other.price
        )


# ---- Test Cases ----

# Product == Product → value comparison
p1 = Product("P1001", 999.99)
p2 = Product("P1001", 999.99)
p3 = Product("P1001", 1099.99)

print(p1 == p2)  # True
print(p1 == p3)  # False

# Product == non-Product → safe comparison
print(p1 == "P1001")   # False
print(p1 == 999.99)    # False

'''
# Key Points (What This Solution Demonstrates)
- Implements a safe and correct __eq__ method.
- Uses isinstance(other, Product) to guard comparisons.
- Returns NotImplemented for non-Product comparisons.
- Compares values only when both objects are Product instances.
- Equality is based on product_id AND price.

# Key Points (Why Returning NotImplemented Matters)
- Signals Python that comparison is unsupported for this type.
- Allows Python to:
  - Try reverse comparison, or
  - Safely return False
- Prevents unexpected errors in mixed-type comparisons.
- This is the Python-recommended behavior for __eq__.

# Key Points (Behavior Explained)
- Product == Product → value-based comparison.
- Same product_id and price → True.
- Different values → False.
- Product == string/int → safely evaluates to False.
- No exceptions raised for invalid comparisons.

# Key Points (Backend / Real-World Relevance)
- Objects are often compared with user input, IDs, or other types.
- Safe equality avoids crashes in:
  - collections
  - filters
  - conditionals
- Essential for robust domain models.

# Core Takeaway
- __eq__ must be:
  - Type-safe
  - Value-based
  - Non-explosive
- Returning NotImplemented is the correct, professional choice.
'''
