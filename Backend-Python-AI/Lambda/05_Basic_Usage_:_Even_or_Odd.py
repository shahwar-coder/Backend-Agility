'''5. Write a lambda that returns "Even" if a number is even, otherwise "Odd".'''

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
        even_or_odd = lambda x : x%2==0
        result = "Even" if even_or_odd(number) else "Odd"
        print(f"{number} is {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Enter an Integer: 12
# 12 is Even

# Enter an Integer: 23
# 23 is Odd

'''
# Key Points (Solution)
- Uses a lambda to check if a number is even.
- Lambda returns a boolean using modulo (% 2).
- Ternary (conditional) expression maps boolean to "Even" or "Odd".
- Separates input handling from logic.
- Keeps lambda focused on a single, simple condition.

# Key Points (Output)
- Outputs whether the number is Even or Odd.
- Works correctly for both even and odd integers.
- Example outputs:
  - 12 → Even
  - 23 → Odd

# Important Note
- Lambdas should return values, not control flow.
- Combining lambda + ternary keeps logic clean and readable.
'''
