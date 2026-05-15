'''
3. Count Even Numbers
Given a list of integers, use reduce() with a lambda to count how many numbers are even.
'''

from functools import reduce

def main()->None:
    try:
        numbers = [3, 8, 12, 5, 7, 10, 14, 9, 2]
        even_lambda = lambda count, num : count + 1 if num%2==0 else count
        result = reduce(even_lambda, numbers, 0)
        print(f"Count of Even: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()


'''
# Key Points (Solution)
- Uses functools.reduce() to accumulate a count.
- Lambda takes an accumulator (count) and current number.
- Increments count when the number is even.
- Leaves count unchanged for odd numbers.
- Initializer 0 starts the counting process correctly.
- Demonstrates reduce() for non-arithmetic aggregation.

# Key Points (Initializer Concept)
- Initializer 0 is the identity for counting.
- Ensures correct behavior even for empty lists.
- Accumulator always represents the current count.

# Key Points (Output)
- Output is an integer.
- Represents how many even numbers exist in the list.
- Example output: 5

# Important Note
- reduce() can replace loops, but clarity matters.
- sum(1 for x in numbers if x % 2 == 0) is often more readable.
'''
