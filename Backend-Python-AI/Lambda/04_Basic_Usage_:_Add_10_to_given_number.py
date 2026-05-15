'''
4. Create a lambda that adds 10 to a given number.
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
        add_10 = lambda x : x+10
        result = add_10(number)
        print(f"{number} + 10 = {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Enter an Integer: 64
# 64 + 10 = 74

'''
# Key Points (Solution)
- Uses a lambda function to perform a simple arithmetic operation.
- Lambda takes one argument and returns the value increased by 10.
- Keeps logic minimal without defining a full function.
- Separates user input handling from computation.
- Demonstrates clear lambda creation and invocation.

# Key Points (Output)
- Outputs the result of adding 10 to the input number.
- Result is an integer.
- Example output: 64 + 10 = 74

# Important Note
- Lambdas are best suited for short, one-line operations.
- For complex calculations, prefer regular def functions.
'''
