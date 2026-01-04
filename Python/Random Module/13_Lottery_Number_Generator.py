'''
Lottery Number Generator:
Generate `count` unique random numbers.
Each number should be between 1 and 49 (inclusive).
'''

import random
from typing import List

def generate_lottery_numbers(count: int) -> List[int]:
    '''
    Generate `count` unique lottery numbers between 1 and 49
    '''
    if count <= 0:
        raise ValueError("Count must be at least 1")
    if count > 49:
        raise ValueError("Count cannot be greater than 49")
    
    return random.sample(population=range(1, 50), k=count)

def get_user_input() -> int:
    '''
    Take valid user input for number count
    '''
    try:
        count = int(input("How many lottery numbers? "))
        return count
    except ValueError as err:
        raise ValueError("Input should be an integer") from err

def main() -> None:
    try:
        count = get_user_input()
        lottery_numbers = generate_lottery_numbers(count)
        print("Lottery Numbers:", lottery_numbers)
    except ValueError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

# How many lottery numbers? 6
# Lottery Numbers: [44, 31, 12, 47, 13, 8]


'''
# Key Points (Solution)
- Uses random.sample() to generate unique numbers.
- Ensures no duplicates (sampling without replacement).
- Restricts numbers to the range 1–49 (inclusive).
- Validates input count (must be between 1 and 49).
- Clean separation of input handling, logic, and execution.
- Returns a list of integers suitable for lottery-style use.

# Key Points (Output)
- Output is a list of integers.
- All numbers are unique.
- Each number lies between 1 and 49.
- List length equals the requested count.
- Example output: [44, 31, 12, 47, 13, 8]

# Important Note
- random.sample() is ideal for lottery and raffle systems.
- Sorting the result can improve readability if needed.
'''
