'''
2. Generate a random floating-point number between 0 and 1.
'''
import random
def floating_0_1()->float:
    '''
    Generate a floating point number between [0.0 and 1.0)
    '''
    return random.random()

def main()->None:
    result = floating_0_1()
    print(f"Random number between 0 and 1: {result}")
    
if __name__=="__main__":
    main()

# Random number between 0 and 1: 0.3453401557364194

'''
# Key Points (Solution)
- Uses random.random() to generate a float.
- random.random() returns a floating-point number with full precision.
- Output range is [0.0, 1.0).
- The function returns a new random value on each call.
- main() handles execution and printing cleanly.

# Key Points (Output)
- Output is a floating-point number.
- Decimal looks long because Python uses 64-bit (IEEE-754) float precision.
- Python does NOT auto-round floating-point values.
- Python prints enough digits to represent the number accurately.
- Value changes on every run (unless seed is fixed).
- Example output: 0.3453401557364194
'''
