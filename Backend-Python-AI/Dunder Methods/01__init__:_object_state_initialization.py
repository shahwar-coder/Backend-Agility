'''
TASK 1: INITIALIZING OBJECT STATE

Write a class `Product` with an __init__ method that:
- Accepts `id` and `price`
- Stores them as instance attributes
- Creates two Product objects with different values
- Prints their attributes

RULES:
- Do NOT create any other methods
- Use __init__ only to set up the object state

GOAL:
Reinforce that __init__ runs after object creation
and is responsible for initializing attributes.
'''

class Product:
    def __init__(self, product_id, price): # I did not use `id` because by same name there is a function `id()`
        self.product_id = product_id
        self.price = price


product1 = Product(1, 2200)
product2 = Product(2, 2300)

print(
    f"product1 details:\n"
    f" Product ID    : {product1.product_id}\n"
    f" Product Price : {product1.price}"
)

print(
    f"product2 details:\n"
    f" Product ID    : {product2.product_id}\n"
    f" Product Price : {product2.price}"
)


# product1 details:
#  Product ID    : 1
#  Product Price : 2200
# product2 details:
#  Product ID    : 2
#  Product Price : 2300

'''
# Key Points (Solution)
- `Product` is a simple class with only an `__init__` method.
- `__init__` accepts `product_id` and `price` as inputs.
- These values are stored on the object using `self`.
- No other methods are defined, strictly following the rules.
- Two separate objects are created with different values.

# Key Points (Why `__init__` Matters)
- Object is first created in memory → then `__init__` is called.
- `__init__` is responsible for initializing object state.
- Each object gets its own independent attributes.
- Changing one object does not affect the other.

# Key Points (Design Choices)
- Used `product_id` instead of `id` to avoid shadowing Python’s built-in `id()` function.
- Attributes are accessed directly (`object.attribute`) for clarity.
- Printing outside the class keeps responsibilities clean.

# Key Points (Output)
- Confirms that both objects hold different state.
- Shows that `__init__` runs separately for each object.
- Demonstrates instance-level data, not class-level data.

# Core Takeaway
- `__init__` does NOT create the object.
- It initializes the object *after* creation.
- Every object gets its own initialized state.
'''
