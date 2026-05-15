'''
4. Concatenate Sentences
Given a list of short strings, 
use reduce() and lambda to combine them into a single sentence, separated by a single space.
'''

from functools import reduce

def main()->None:
    try:
        words = ["Learning", "functional", "programming", "with", "Python"]
        concatenate_lambda = lambda sentence, word :  sentence + " " + word
        result = reduce(concatenate_lambda, words) # initializer not required here
        print(f"Concatenated words => Sentence => {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Concatenated words => Sentence => Learning functional programming with Python

'''
# Key Points (Solution)
- Uses functools.reduce() to build a sentence incrementally.
- Lambda combines the accumulated sentence with the next word.
- Adds a single space between words during concatenation.
- No initializer is required because the list is non-empty.
- Demonstrates reduce() for string aggregation tasks.

# Key Points (Accumulator Flow)
- First word becomes the initial accumulator.
- Each subsequent word is appended with a space.
- Accumulator grows into a full sentence step by step.

# Key Points (Output)
- Output is a single string.
- Words are joined with exactly one space.
- Order of words is preserved.
- Example output: "Learning functional programming with Python"

# Important Note
- For production code, " ".join(words) is simpler and faster.
- reduce() is useful here for learning accumulator-based logic.
'''
