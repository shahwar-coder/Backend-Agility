'''
18. Given a list of dictionaries with key "price", sort the list by price in ascending order using lambda.
'''

def main()->None:
    try:
        data = [
                {"item": "Laptop", "price": 75000},
                {"item": "Smartphone", "price": 32000},
                {"item": "Headphones", "price": 2500},
                {"item": "Monitor", "price": 18000},
                {"item": "Keyboard", "price": 1200},
                {"item": "Mouse", "price": 800}]
        price_key = lambda x : x.get("price")
        result = sorted(data, key=price_key)
        print(f"Sorted by price: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

'''
# Key Points (Solution)
- Uses sorted() to order a list of dictionaries.
- Lambda function extracts the "price" value from each dictionary.
- key= argument tells sorted() to sort based on price.
- Sorting is done in ascending order by default.
- Original list remains unchanged; a new sorted list is returned.
- Lambda keeps the key logic short and readable.

# Key Points (Output)
- Output is a list of dictionaries.
- Items are ordered from lowest price to highest.
- Each dictionary structure is preserved.
- Example output starts with:
  {"item": "Mouse", "price": 800}

# Important Note
- Using dict.get() avoids KeyError if the key is missing.
- Lambdas are ideal for simple key-extraction logic.
'''
