'''
5. Create a list of 10 random integers between 1 and 100, and print them all.
'''

from typing import Tuple, List
import random

def list_of_10(a: int, b: int)->List[int]:
    '''
    Create list of 10 random numers
    '''
    if a>b:
        raise ValueError("a must be lesser than b.")
        
    return [random.randint(a, b) for _ in range(10)]

def get_user_input()->Tuple[int, int]:
    '''
    Take valid inputs
    '''
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        return a, b
    except ValueError as err:
        raise ValueError("Inputs must be integers") from err

def main()->None:
    try:
        a, b = get_user_input()
        result = list_of_10(a, b)
        print(f"List of random integers between 1 and 100: {result}")
    except ValueError as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()
    
# Enter a: 1
# Enter b: 100

'''
# Key Points (Solution)
- Uses list comprehension for concise and efficient list creation.
- random.randint(a, b) generates each random integer.
- Generates exactly 10 numbers.
- Validates input range (a <= b).
- Clean separation of input, logic, and execution.
- Returns a list, not a generator, since all values are needed at once.

# Key Points (Output)
- Output is a list containing 10 integers.
- Each number lies between a and b (inclusive).
- Values may repeat.
- Order is random on every run (unless seed is fixed).
- Example output: [19, 74, 50, 49, 63, 94, 45, 61, 76, 100]

# Important Note
- List comprehension is preferred for simple fixed-size collections.
- Printing the list shows all generated values at once.
'''

# List of random integers between 1 and 100: [19, 74, 50, 49, 63, 94, 45, 61, 76, 100]
    
