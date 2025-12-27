'''
4. Print 5 random numbers between 10 and 50 using a loop.
'''
from typing import Tuple, Generator
import random
def five_random_numbers(a: int, b: int, count: int = 5)->Generator[int, None, None]:
    '''
    Yield 5 random numbers
    '''
    # we choose randint over randrange, as specific steps for even/odd not required
    if a>b:
        raise ValueError("a must be less than b")
    
    for _ in range(count):
        yield random.randint(a, b)
        

def get_user_input()->Tuple[int, int]:
    '''
    Take valid user inputs
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
        # here I have to collect and print generator values....
        for num in five_random_numbers(a, b):
            print(num)
    except ValueError as err:
        print(f"Error: {err}")
        

if __name__=="__main__":
    main()
        
# Enter a: 10
# Enter b: 50
# 35
# 19
# 33
# 38
# 31
if __name__=="__main__":
    main()


'''
# Key Points (Solution)
- Uses a loop with random.randint(a, b) to generate numbers.
- Generates exactly 5 random integers by default (count=5).
- Implements a generator (yield) for memory-efficient iteration.
- Validates input range (a <= b) before generation.
- Separates logic, input handling, and execution clearly.
- randint is chosen since no step control (even/odd) is needed.

# Key Points (Output)
- Outputs 5 integers.
- Each number lies between a and b (inclusive).
- Numbers are independent and may repeat.
- Output order matches generation order.
- Example output: 35, 19, 33, 38, 31

# Important Note
- Generators produce values one at a time, not all at once.
- Looping over the generator automatically retrieves each value.
'''
