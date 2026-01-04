'''
Dice Roll Simulation:
Write a program that simulates rolling a six-sided die 10 times.
Display the result of each roll.
'''
import random
from typing import Generator

def roll_simulation(rolls: int)->Generator[int, None, None]:
    '''
    Roll Dice `rolls` times
    '''
    if rolls <= 0:
        raise ValueError("You roll atleast once")
    for _ in range(rolls):
        # yield random.choices(population=[1,2,3,4,5,6], k=1) # okay, but will yield sub-list form not ints, eg. [1], [4]..etc
        yield random.randint(1, 6)

def get_user_input()->int:
    '''
    Take valid user imput
    '''
    try:
        rolls = int(input("How many times you want to roll?"))
        return rolls
    except ValueError as err:
        raise ValueError("Input should be an integer") from err

def main()->None:
    try:
        rolls = get_user_input()
        for roll in roll_simulation(rolls):
            print(roll)
    except (ValueError) as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# How many times you want to roll?10
# 5
# 3
# 2
# 5
# 5
# 1
# 1
# 5
# 2
# 2

'''
# Key Points (Solution)
- Simulates rolling a six-sided die using random.randint(1, 6).
- Uses a generator (yield) to produce one roll at a time.
- Validates that the number of rolls is greater than zero.
- Separates user input, dice logic, and execution clearly.
- Uses randint instead of choices to return integers directly.
- Memory-efficient approach using a generator.

# Key Points (Output)
- Prints one die result per line.
- Each value is an integer between 1 and 6 (inclusive).
- Results are independent and random.
- Total outputs equal the number of rolls requested.
- Example output: 3, 6, 1, 4, ...

# Important Note
- Generators are ideal for sequential simulations.
- Setting a random seed can make results reproducible.
'''
