'''
5. Create a color palette (["red", "blue", "green", "yellow", "black", "white"]) and randomly select a color.
'''

import random
from typing import List


def random_color() -> str:
    """
    Randomly select and return a color from the palette.
    """
    palette: List[str] = ["red", "blue", "green", "yellow", "black", "white"]
    return random.choice(palette)


def main() -> None:
    color = random_color()
    print(f"Selected color: {color}")


if __name__ == "__main__":
    main()

# Selected color: yellow


'''
# Key Points (Solution)
- Defines a fixed color palette as a list of strings.
- Uses random.choice() to select one color randomly.
- No user input required; palette is predefined.
- Simple and clean function returning a single value.
- Suitable for random selection from small fixed datasets.

# Key Points (Output)
- Output is a single color name (string).
- Selected color always comes from the palette.
- Result changes on each run (unless seed is fixed).
- Example output: "yellow"

# Important Note
- random.choice() works with any non-empty sequence.
- Raises an error if the palette list is empty.
'''
