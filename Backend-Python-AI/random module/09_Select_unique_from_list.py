'''
4. From a list of 20 numbers, select 5 random numbers without replacement.
'''

import random
from typing import List, Tuple
def select_unique(numbers: List[int], select: int)->List[int]:
    '''
    Select k numbers from the given list of numbers (uniquely)
    '''
    if select>len(numbers):
        raise ValueError("You cannot select more numbers than total numbers.")
    return random.sample(population=numbers, k=select)

def get_user_input()->Tuple[List[int], int]:
    '''
    Take valid inputs
    '''
    try:
        count = int(input("How many numbers in list: "))
        numbers: List[int] = []
        select = int(input("How many numbers to select from the list: "))
        
        for i in range(count):
            number = int(input(f"Enter number {i}: "))
            numbers.append(number)
        return numbers, select
    except ValueError as err:
        raise ValueError("Count and Numbers must be integers") from err

def main()->None:
    try:
        numbers, select = get_user_input()
        result = select_unique(numbers, select)
        print(f"{select} Unique Numbers: {result}")
    except ValueError as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()
    
    

# How many numbers in list: 20
# How many numbers to select from the list: 5
# Enter number 0: 1
# Enter number 1: 2
# Enter number 2: 3
# Enter number 3: 4
# Enter number 4: 5
# Enter number 5: 6
# Enter number 6: 7
# Enter number 7: 8
# Enter number 8: 9
# Enter number 9: 10
# Enter number 10: 11
# Enter number 11: 12
# Enter number 12: 13
# Enter number 13: 14
# Enter number 14: 15
# Enter number 15: 16
# Enter number 16: 17
# Enter number 17: 18
# Enter number 18: 19
# Enter number 19: 20
# 5 Unique Numbers: [19, 6, 13, 12, 8]

'''
# Key Points (Solution)
- Uses random.sample() to select numbers without replacement.
- Guarantees all selected numbers are unique.
- Validates that select ≤ total numbers in the list.
- Original list remains unchanged.
- Clean separation of input handling, logic, and execution.
- Ideal for lottery-like or fair selection scenarios.

# Key Points (Output)
- Output is a list of integers.
- List length equals the requested selection count (e.g., 5).
- No duplicates appear in the result.
- Order of selected numbers is random.
- Example output: [19, 6, 13, 12, 8]

# Important Note
- random.sample() is preferred over repeated randint() calls
  when uniqueness is required.
'''
