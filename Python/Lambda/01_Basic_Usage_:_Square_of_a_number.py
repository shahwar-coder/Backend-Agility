'''
1. Create a lambda that returns the square of a number and use it to square 7.
'''

def main()->None:
    try:
        number = 7
        square = lambda number: number**2 # square is the function name (Always define function name first), you can also write : x: x**2 , as we are sending number when calling the fuction, and it will be automatically mapped to x.
        result = square(number) # calling the function
        print(f"Number: {number}, Square: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Number: 7, Square: 49

'''
# Key Points (Solution)
- Uses a lambda to define a short, single-expression function.
- Lambda is assigned to a variable name (square), just like a normal function.
- Parameter name inside lambda is flexible (number or x both work).
- Argument passed during the call is automatically mapped to the lambda parameter.
- Avoids using def for simple, one-line logic.
- Demonstrates clear function creation and invocation flow.

# Key Points (Output)
- Prints the original number and its square.
- Output is an integer value.
- Example output: Number: 7, Square: 49

# Important Note
- Lambda parameters are positional, not name-dependent.
- Use lambdas for small operations; prefer def for complex logic.
'''

