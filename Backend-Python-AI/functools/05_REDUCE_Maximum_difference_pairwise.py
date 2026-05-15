'''READ THIS SOLUTION CAREFULLY (very interesting)
5. Maximum Difference Pairwise
Given a list of integers, use reduce() with a lambda to compute
the maximum difference between consecutive elements.
'''

from functools import reduce

def main() -> None:
    try:
        numbers = [10, 3, 15, 7, 20, 12]

        # compute consecutive differences
        differences = [
            abs(numbers[i] - numbers[i - 1])
            for i in range(1, len(numbers))
        ]

        max_difference = reduce(lambda a, b: a if a > b else b, differences)
        print(f"Maximum difference between consecutive elements: {max_difference}")

    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

'''
# Key Points (Solution)
- Breaks the problem into two clear steps:
  1) Compute differences between consecutive elements.
  2) Reduce those differences to find the maximum.
- Uses a list comprehension to calculate absolute differences.
- abs() ensures difference magnitude, not direction.
- reduce() compares two values at a time to keep the maximum.
- Lambda acts like a manual max() function.
- Demonstrates how reduce() works best on already-derived data.

# Key Points (Reducer Logic)
- Accumulator (a) holds the current maximum difference.
- Current value (b) is compared against it.
- Larger value is carried forward.
- Final accumulator is the maximum difference.

# Key Points (Output)
- Output is a single integer.
- Represents the maximum absolute difference
  between consecutive list elements.
- Example output: 13

# Important Note
- Preprocessing data before reduce() often improves clarity.
- Built-in max(differences) is simpler,
  but reduce() helps understand comparison-based accumulation.
'''

