'''
6. Using map() and lambda, convert a list of temperatures in Celcius
[0, 10, 20, 30] into Fahrenheit.
'''

def main()->None:
    try:
        temperatures = [0, 10, 20, 30]
        celcius_to_farenheit = lambda x : x*9/5 + 32
        result = list(map(celcius_to_farenheit, temperatures))
        print(f"Converted Temperatures: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Converted Temperatures: [32.0, 50.0, 68.0, 86.0]

'''
# Key Points (Solution)
- Uses lambda to define the Celsius → Fahrenheit conversion formula.
- Applies the lambda to each element using map().
- map() processes the list element-by-element.
- Converts the map object to a list for display.
- Avoids explicit loops for cleaner functional-style code.

# Key Points (Output)
- Output is a list of floating-point values.
- Each value represents the Fahrenheit equivalent.
- Order matches the original Celsius list.
- Example output: [32.0, 50.0, 68.0, 86.0]

# Important Note
- map() is ideal when the same transformation applies to all items.
- Lambdas keep transformations concise and readable.
'''
