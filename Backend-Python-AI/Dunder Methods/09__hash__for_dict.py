'''
TASK 2: HASH BASED ON IMMUTABLE DATA ONLY

Write a class `Product` with:
- Attributes: product_id and price
- __eq__ compares only product_id
- __hash__ uses only product_id

TEST CASES TO CONSIDER:
- Two Products with same product_id but different prices
  should be treated as the same key in a dictionary

RULES:
- Use only immutable attributes for hashing
- Ensure hash value does not change during object lifetime

GOAL:
Understand what makes a safe and correct __hash__ implementation.
'''

class Product:
    """Product identified uniquely by product_id"""

    def __init__(self, product_id: str, price: float) -> None:
        self.product_id = product_id
        self.price = price

    def __repr__(self) -> str:
        return f"Product(product_id={self.product_id!r}, price={self.price!r})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.product_id == other.product_id

    def __hash__(self) -> int:
        # Hash ONLY immutable identity field
        return hash(self.product_id)


# ------------------- TEST CASES -------------------

product1 = Product("P1001", 75000)
product2 = Product("P1001", 82000)   # same ID, different price
product3 = Product("P2002", 45000)

# Dictionary usage
products_dict = {
    product1: "Laptop - Old Price",
    product2: "Laptop - Updated Price",
    product3: "Monitor",
}

print(products_dict)
print("Total keys:", len(products_dict))

# Output:
# {
#  Product(product_id='P1001', price=75000): 'Laptop - Updated Price',
#  Product(product_id='P2002', price=45000): 'Monitor'
# }
# Total keys: 2


'''
# Key Points (What This Implementation Demonstrates)
- __eq__ defines equality based ONLY on product_id.
- price is intentionally ignored for equality comparison.
- Two Product objects with the same product_id are considered the same logical entity.

# Key Points (Why __hash__ Uses Only product_id)
- Hashing MUST rely on immutable data.
- product_id is immutable and uniquely identifies a Product.
- price is mutable → unsafe for hashing.
- Using only product_id ensures hash stability for the object’s lifetime.

# Key Points (Correctness Contract)
- Equality rule:
    product1 == product2  ⇨  product1.product_id == product2.product_id
- Hash rule:
    hash(product1) == hash(product2) ⇨ hash(product_id)

- This satisfies Python’s rule:
    if a == b  →  hash(a) == hash(b)

# Key Points (Observed Behavior in Dictionary)
- product1 and product2 share the same key (same product_id).
- product2 overwrites product1’s value.
- Dictionary ends up with only ONE entry for product_id="P1001".
- product3 has a different product_id → separate key.

# Key Points (Why This Is Backend-Safe)
- Prevents hash corruption due to mutable fields.
- Enables reliable use of Product as:
  - dict keys
  - set elements
  - cache identifiers
- Mirrors real-world domain logic:
  product_id = identity, price = attribute.

# Core Takeaway
- __hash__ must use ONLY immutable identity data.
- __eq__ and __hash__ must describe the SAME identity.
- Mutable fields should NEVER participate in hashing.
'''
