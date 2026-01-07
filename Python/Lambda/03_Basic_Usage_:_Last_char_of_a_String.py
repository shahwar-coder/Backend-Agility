'''
3. Write a lambda that returns the last character of a string.
'''

def get_user_input()->int:
    '''
    Ensure taking valid user input
    '''
    try:
        word = input("Enter String (word): ")
        return word
    except Exception as err:
        raise Exception("Error") from err

def main()->None:
    try:
        word = get_user_input()
        if not word:
            raise ValueError("Input string cannot be empty")
        get_last_char = lambda x : x[-1]
        result = get_last_char(word)
        print(f"Last character of {word} -> {result}")
    except ValueError as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Enter String (word): Shahwar
# Last character of Shahwar -> r

# Enter String (word): 
# Error: Input string cannot be empty

'''
# Key Points (Solution)
- Uses a lambda function to extract the last character of a string.
- Lambda accesses the last element using negative indexing (x[-1]).
- Validates that the input string is not empty before applying the lambda.
- Separates input handling from processing logic.
- Demonstrates safe usage of lambdas with basic validation.

# Key Points (Output)
- Outputs a single character.
- Character is the last character of the input string.
- Raises an error for empty input strings.
- Example output: "r" for input "Shahwar".

# Important Note
- Negative indexing is a Pythonic way to access elements from the end.
- Always validate input before indexing to avoid runtime errors.
'''
