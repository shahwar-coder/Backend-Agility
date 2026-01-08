'''
8. Using map() and lambda, find the length of each word in the list
["apple", "banana", "kiwi"].
'''

def main()->None:
    try:
        fruits = ["apple", "banana", "kiwi"]
        calculate_length_of_fruits = lambda x : len(x)
        result = list(map(calculate_length_of_fruits, fruits))
        for fruit, length in zip(fruits, result):
            print(f"{fruit} : {length}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# apple : 5
# banana : 6
# kiwi : 4


'''
# Key Points (Solution)
- Uses a lambda function to compute the length of a string.
- Applies the lambda to each word using map().
- map() transforms each element independently.
- zip() is used to pair original words with their lengths.
- Avoids explicit indexing and keeps code readable.

# Key Points (Output)
- Prints each word with its corresponding length.
- Lengths correctly reflect the number of characters.
- Output order matches the original list.
- Example output:
  apple : 5
  banana : 6
  kiwi : 4

# Important Note
- map() is ideal for one-to-one transformations.
- zip() is useful for parallel iteration over related sequences.
'''

