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
