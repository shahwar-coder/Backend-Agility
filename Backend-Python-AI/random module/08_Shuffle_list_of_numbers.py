'''
3. Shuffle a list of numbers from 1 to 10 and print the shuffled result.
'''
import random
from typing import List
def shuffle_numbers(numbers: List[int])->List[int]:
    '''
    Shuffle the given list of numbers
    '''
    # return random.shuffle(numbers) # here we can't return directly, it's an inplace operation, return numbers list instead
    random.shuffle(numbers)
    return numbers

def get_user_input()->List[int]:
    '''
    Take valid inputs
    '''
    try:
        count = int(input("How many numbers in list: "))
        numbers: List[int] = []
        
        for i in range(count):
            number = int(input(f"Enter number {i}: "))
            numbers.append(number)
        return numbers
    except ValueError as err:
        raise ValueError("Count and Numbers must be integers") from err

def main()->None:
    try:
        numbers = get_user_input()
        result = shuffle_numbers(numbers)
        print(f"Shuffled Numbers: {result}")
    except ValueError as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()
    


# How many numbers in list: 10
# Enter number 0: 23
# Enter number 1: 45
# Enter number 2: 6
# Enter number 3: 67
# Enter number 4: 8
# Enter number 5: 98
# Enter number 6: 7
# Enter number 7: 54
# Enter number 8: 321
# Enter number 9: 444
# Shuffled Numbers: [98, 45, 7, 67, 54, 23, 6, 444, 8, 321]

'''
# Key Points (Solution)
- Uses random.shuffle() to randomly reorder list elements.
- shuffle() works in-place and does NOT return a new list.
- Function returns the same list after shuffling.
- Input is collected dynamically from the user.
- Clean separation of input, logic, and execution.
- Suitable when list order needs to be randomized.

# Key Points (Output)
- Output is a shuffled list of integers.
- Contains the same elements as the original list.
- Order is random on every run (unless seed is fixed).
- Length of list remains unchanged.
- Example output: [98, 45, 7, 67, 54, 23, 6, 444, 8, 321]

# Important Note
- Since shuffle() mutates the list, keep a copy if original order is needed.
- Use random.sample(list, k=len(list)) for a non-mutating shuffle.
'''
