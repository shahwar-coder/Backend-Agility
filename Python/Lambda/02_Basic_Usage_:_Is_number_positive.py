'''
2. Write a lambda that checks whether a number is positive.
'''

def get_user_input()->int:
    '''
    Ensure taking valid user input
    '''
    try:
        number = int(input("Enter an Integer: "))
        return number
    except ValueError as err:
        raise ValueError("Input should be valid integer") from err

def main()->None:
    try:
        number = get_user_input()
        is_positive = lambda x : x>0
        result = is_positive(number)
        print(f"Is {number} positive ? {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Enter an Integer: 12
# Is 12 positive ? True

# Enter an Integer: 0
# Is 0 positive ? False

# Enter an Integer: -23
# Is -23 positive ? False

'''
# Key Points (Solution)
- Uses a lambda function to perform a simple boolean check.
- Lambda takes one argument and returns True if the number is greater than 0.
- Demonstrates how lambdas return boolean expressions directly.
- Separates user input handling from logic.
- Avoids defining a full function for a one-line condition.

# Key Points (Output)
- Output is a boolean value (True or False).
- Positive numbers return True.
- Zero and negative numbers return False.
- Example outputs:
  - 12 → True
  - 0 → False
  - -23 → False

# Important Note
- Lambdas are ideal for short conditional checks.
- For multi-condition or complex validation, use def instead.
'''
