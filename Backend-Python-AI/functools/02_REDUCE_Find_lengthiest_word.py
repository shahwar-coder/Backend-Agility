'''
2. Longest Word Length
Given a list of strings, use reduce() and lambda to find the maximum length among all words.
'''

from functools import reduce

def main()->None:
    try:
        words = ["python", "lambda", "reduce", "functional", "clean", "code"]
        lengthiest_word_lambda = lambda a, b : a if len(a)>len(b) else b # max() : can also be used here, no problem
        result = reduce(lengthiest_word_lambda, words, "")
        print(f"Lengthiest word is: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Lengthiest word is: functional

'''
DRY RUN of reduce(lambda a, b: a if len(a) > len(b) else b, words, "")

words = ["python", "lambda", "reduce", "functional", "clean", "code"]

Initializer:
a = ""                      # len = 0

Iteration 1:
b = "python"                # len = 6
len(a) > len(b) → 0 > 6 → False
return b → "python"
a = "python"

Iteration 2:
b = "lambda"                # len = 6
len(a) > len(b) → 6 > 6 → False
return b → "lambda"
a = "lambda"

Iteration 3:
b = "reduce"                # len = 6
len(a) > len(b) → 6 > 6 → False
return b → "reduce"
a = "reduce"

Iteration 4:
b = "functional"            # len = 10
len(a) > len(b) → 6 > 10 → False
return b → "functional"
a = "functional"

Iteration 5:
b = "clean"                 # len = 5
len(a) > len(b) → 10 > 5 → True
return a → "functional"
a = "functional"

Iteration 6:
b = "code"                  # len = 4
len(a) > len(b) → 10 > 4 → True
return a → "functional"
a = "functional"

Final Result:
result = "functional"
'''


# =======================================


'''
# Key Points (Solution)
- Uses functools.reduce() to compare elements cumulatively.
- Lambda compares two words and keeps the longer one.
- At each step, the longer word becomes the new accumulator.
- Initializer "" (empty string) ensures safe comparison.
- Avoids explicit loops for a clean functional approach.
- Logic is equivalent to finding max by length.

# Key Points (Initializer Concept)
- Initializer "" acts as a safe starting value.
- Empty string length is 0, so any real word replaces it.
- Prevents errors if the list were empty.
- Similar to using identity values in reduce().

# Key Points (Output)
- Output is a single string.
- Represents the longest word in the list.
- Example output: "functional"

# Important Note
- reduce() is useful for custom aggregation logic.
- Built-in max(words, key=len) is simpler for real-world use,
  but reduce() helps understand accumulator-based thinking.
'''
