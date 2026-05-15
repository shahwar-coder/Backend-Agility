'''
1. Product of Prices
Given a list of item prices as integers, use reduce() with a lambda to calculate the total product of all prices.
(Assume the list is non-empty.)
'''

from functools import reduce

def main()->None:
    try:
        prices = [1200, 450, 999, 250, 1800]
        price_product_lambda = lambda acc, x : acc * x 
        result = reduce(price_product_lambda, prices, 1)
        print(f"Product of Prices: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Product of Prices: 242757000000000

'''
- 1 here is initializer
- everything further multiplies to it, it starts the multiplication
- Why 1 specifically ?
    - Because 1 is the identity for multiplication:
        1 * x = x

        Just like:
        0 is identity for addition
        1 is identity for multiplication
'''
# ===================================================
'''
# Key Points (Solution)
- Uses functools.reduce() to combine all list elements into a single value.
- Lambda takes two arguments: accumulator (acc) and current value (x).
- On each step, acc * x is computed and passed forward.
- Since the list is non-empty, reduce() works without an initializer.
- Clean functional approach for cumulative operations like product.

# Key Points (Initializer Concept)
- An initializer (e.g., 1) can be passed as the third argument to reduce().
- Initializer is the starting value of the accumulator.
- 1 is used because it is the identity for multiplication:
  - 1 * x = x
- Similar concept:
  - 0 is the identity for addition
  - 1 is the identity for multiplication
- Initializers are especially important for empty lists.

# Key Points (Output)
- Output is a single integer.
- Represents the product of all prices.
- Example output: 242757000000000

# Important Note
- reduce() is best suited for cumulative operations.
- Always choose the correct identity value when using an initializer.
'''
