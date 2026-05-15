'''11. Use filter() and lambda to keep only even numbers from a list.'''

def main()->None:
    try:
        numbers = [1,2,3,4,5,6,7,8,9,10]
        only_even = lambda x : x%2==0
        result = list(filter(only_even, numbers))
        print(f"Even numbers filtered : {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Even numbers filtered : [2, 4, 6, 8, 10]

'''
# Key Points (Solution)
- Uses a lambda function to test whether a number is even.
- Applies the lambda as a predicate inside filter().
- filter() keeps only elements for which the lambda returns True.
- Converts the filter object to a list for display.
- Avoids manual loops for cleaner functional-style code.

# Key Points (Output)
- Output is a list of even integers.
- All odd numbers are removed.
- Order of numbers is preserved from the original list.
- Example output: [2, 4, 6, 8, 10]

# Important Note
- filter() is best suited for selection based on conditions.
- Lambdas keep predicate logic short and expressive.
'''
