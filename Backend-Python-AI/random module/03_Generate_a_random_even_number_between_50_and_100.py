'''
3. Generate a random even number between 50 and 100.
'''
from typing import Tuple
import random

def random_even_in_range(a: int, b: int)->int:
    '''
    Generate even number between a and b , (Eg. 50 and 100)
    '''
    if a>b: # a=51, b=51
        raise ValueError("a must be less than b")
        
    start = a if a%2==0 else a+1 # to be safe we start with even
    end = b if b%2==0 else b-1 # and end with even
    step = 2 # as interested in even
    
    if start>end: # a=51+1, b=51-1
        raise ValueError("No even numbers in the given range")
    
    # start, end, step : for randrange()
    # we choose randrange() over randint(), because...
    # randint() -> can give odds, but we can control randrange() -> to give even, using start, end, step properly.
    return random.randrange(start, end+1, step)


def get_user_input()->Tuple[int, int]:
    '''
    Take valid user inputs
    '''
    try:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        return a, b
    except ValueError as err:
        raise ValueError("Input should be integers") from err

def main()->None:
    try:
        a, b = get_user_input()
        result = random_even_in_range(a, b)
        print(f"Random Even number between {a} and {b} : {result}")
    except ValueError as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()
  
# Enter a: 50
# Enter b: 100
# Random Even number between 50 and 100 : 66

# Enter a: 50
# Enter b: 100
# Random Even number between 50 and 100 : 88

# Enter a: 51
# Enter b: 51
# Error: No even numbers in the given range


'''
# Key Points (Solution)
- Uses random.randrange(start, end+1, step) to control even numbers.
- Adjusts start to the next even number if a is odd.
- Adjusts end to the previous even number if b is odd.
- step = 2 ensures only even numbers are generated.
- Validates range (a <= b) and checks if any even number exists.
- Separates input handling, logic, and execution cleanly.
- Uses randrange instead of randint to avoid odd numbers.

# Key Points (Output)
- Output is always an even integer.
- Value lies between a and b (inclusive).
- Result changes on each run (unless seed is fixed).
- Example outputs: 66, 88.
- Proper error shown when no even numbers exist in range.

# Important Note
- randrange() is ideal when you need controlled stepping (even/odd).
- Defensive checks prevent logical edge-case bugs.
'''
