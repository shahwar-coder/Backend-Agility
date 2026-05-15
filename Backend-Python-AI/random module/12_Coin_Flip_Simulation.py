'''
Coin Flip Simulation:
Simulate flipping a coin 100 times.
Count and print how many times the result is Heads and how many times it is Tails.
'''

import random
from typing import Generator

def flip_coin(flips: int)->Generator:
    '''
    Flip coin `flips` times
    '''
    if flips<=0:
        raise ValueError("You need to make One flip atleast")
    
    for _ in range(flips):
        yield random.choice(["Heads", "Tails"])

def get_user_input()->int:
    '''
    Take valid user input
    '''
    try:
        flips = int(input("How many flips ?"))
        return flips
    except ValueError as err:
        raise ValueError("Input should be an integer") from err

def main()->None:
    try:
        heads = 0
        tails = 0
        flips = get_user_input()
        for coin_face in flip_coin(flips):
            if coin_face=="Heads":
                heads+=1
            else:
                tails+=1
        print(f"Total Heads: {heads} & Total Tails: {tails}")
    except (ValueError) as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# How many flips ?100
# Total Heads: 49 & Total Tails: 51


'''
# Key Points (Solution)
- Simulates coin flips using random.choice(["Heads", "Tails"]).
- Uses a generator to produce one flip result at a time.
- Validates that the number of flips is greater than zero.
- Counts Heads and Tails using simple counters.
- Separates input handling, simulation logic, and counting clearly.
- Generator-based approach is memory efficient.

# Key Points (Output)
- Prints total counts of Heads and Tails.
- Sum of Heads and Tails equals total flips.
- Results vary on each run due to randomness.
- Example output: Total Heads: 49 & Total Tails: 51

# Important Note
- Results approach 50–50 distribution as flips increase.
- Setting a random seed can make outcomes reproducible.
'''
