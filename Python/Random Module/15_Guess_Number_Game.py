'''
Guess the Number Game:
The computer randomly selects a number between 1 and 50.
The user keeps guessing until the correct number is found.
After each guess, display whether the guess is "Too High" or "Too Low".
'''

import random


def generate_secret_number() -> int:
    """
    Generate a random number between 1 and 50 (inclusive).
    """
    return random.randint(1, 50)


def get_user_guess() -> int:
    """
    Take a valid integer guess from the user.
    """
    try:
        return int(input("Enter your guess (1–50): "))
    except ValueError as err:
        raise ValueError("Guess must be an integer") from err


def play_game(secret_number: int) -> None:
    """
    Run the guessing loop until the user guesses correctly.
    """
    while True:
        try:
            guess = get_user_guess()

            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50.")
                continue

            if guess < secret_number:
                print("Too Low")
            elif guess > secret_number:
                print("Too High")
            else:
                print("Correct! You guessed the number.")
                break

        except ValueError as err:
            print(f"Error: {err}")


def main() -> None:
    secret_number = generate_secret_number()
    play_game(secret_number)


if __name__ == "__main__":
    main()

# Enter your guess (1–50): 2
# Too Low
# Enter your guess (1–50): 3
# Too Low
# Enter your guess (1–50): 5
# Too Low
# Enter your guess (1–50): 8
# Too Low
# Enter your guess (1–50): 45
# Too High
# Enter your guess (1–50): 34
# Too Low
# Enter your guess (1–50): 37
# Too Low
# Enter your guess (1–50): 40
# Correct! You guessed the number.


'''
# Key Points (Solution)
- Generates a secret number using random.randint(1, 50).
- Uses a loop to allow repeated guesses until correct.
- Validates that guesses are within the allowed range.
- Provides feedback after each guess: "Too Low", "Too High", or "Correct".
- Handles invalid (non-integer) input gracefully.
- Separates number generation, input handling, and game logic.

# Key Points (Output)
- Continuously prints feedback after each guess.
- Stops only when the correct number is guessed.
- Final message confirms the correct guess.
- Output depends on user input and random secret number.

# Important Note
- Infinite loop (while True) is suitable for games with unknown attempts.
- Game can be extended by adding attempt counters or hints.
'''
