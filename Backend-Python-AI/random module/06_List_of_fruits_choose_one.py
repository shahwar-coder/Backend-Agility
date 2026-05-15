'''
1. Create a list of fruits and print a random fruit each time you run the program.
'''


from typing import List
import random

def select_fruits(fruits: List[str])->List[int]:
    '''
    Choose 1 fruit from fruits
    '''
    return random.choice(seq=fruits)

def get_user_input()->List[int]:
    '''
    Take valid inputs
    '''
    try:
        total_fruits = int(input("Total fruits in your basket: "))
        return [input() for _ in range(total_fruits)]
    except ValueError as err:
        raise ValueError("Total fruits must be an integer") from err

def main()->None:
    try:
        fruits = get_user_input()
        result = select_fruits(fruits)
        print(f"Your random fruit: {result}")
    except ValueError as err:
        print(f"Error: {err}")
    
if __name__=="__main__":
    main()
    
# Total fruits in your basket: 5
# apple
# banana
# guava
# cherry
# avocado
# Your random fruit: banana

'''
# Key Points (Solution)
- Uses random.choice() to select one item from a list.
- Fruits are stored as a list of strings.
- User dynamically inputs the list size and fruit names.
- random.choice() ensures only one fruit is selected each run.
- Clean separation of input, selection logic, and execution.
- Suitable for non-numeric random selection.

# Key Points (Output)
- Output is a single fruit name (string).
- Fruit is always chosen from the given list.
- Result changes on every run (unless seed is fixed).
- Example output: "banana"

# Important Note
- random.choice() works with any sequence (list, tuple, string).
- Raises an error if the list is empty, so input size matters.
'''

    
