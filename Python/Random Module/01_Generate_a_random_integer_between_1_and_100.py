'''
1. Generate a random integer between 1 and 100.
'''

import random
from typing import Tuple

def random_a_and_b(a: int, b: int)->int:
    '''
    Generate a random number between a and b (eg. 1 and 100)
    '''
    if a>b:
        raise ValueError("a must be less than or equal to b")
    return random.randint(a, b)
    
def get_user_input() -> Tuple[int, int]:
    '''
    Read user inputs
    '''
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        return a,b
    except ValueError as err:
        raise ValueError("Input must be valid integers") from err
        
def main() -> None:
    try:
        a, b = get_user_input()
        result = random_a_and_b(a, b)
        print(f"Random Number between {a} and {b} : {result}")
    except ValueError as err:
        print(f"Error: {err}")
        
if __name__ == "__main__":
    main()
    
# Enter a: 1
# Enter b: 100
# Random Number between 1 and 100 : 71


'''
# Key Points (Solution)
- Uses random.randint(a, b) to generate a random integer.
- Both a and b are inclusive (can appear in output).
- Validates range: raises error if a > b.
- User input is separated into its own function for clarity.
- Proper error handling for invalid (non-integer) inputs.
- main() controls program flow and handles exceptions.

# Key Points (Output)
- Output is an integer.
- Value is always between a and b (inclusive).
- Number changes on every run (unless seed is fixed).
- Example output: 71

# Important Note
- random.randint() is suitable when you need whole numbers.
- Input validation prevents logical and runtime errors.
'''

