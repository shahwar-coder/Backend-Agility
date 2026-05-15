'''
16. Sort a list of tuples (name, age) by age using sorted() and lambda.
'''

def main() -> None:
    try:
        indian_actors = [
                ("Shah Rukh Khan", 59),
                ("Aamir Khan", 60),
                ("Salman Khan", 59),
                ("Amitabh Bachchan", 82),
                ("Akshay Kumar", 57),
                ("Hrithik Roshan", 51),
                ("Ranbir Kapoor", 42),
                ("Ranveer Singh", 39),
                ("Ajay Devgn", 56),
                ("Kartik Aaryan", 34)
            ]

        age_key = lambda x: x[1] # because at index 1 -> 2nd element of every tuple is age.
        result = sorted(indian_actors, key=age_key) # here, writing `key=` is very important (keyword argument is imp for key) 
        print(f"Indian actors sorted by age: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()


# Indian actors sortd by age: [('Kartik Aaryan', 34), 
#                              ('Ranveer Singh', 39), 
#                              ('Ranbir Kapoor', 42), 
#                              ('Hrithik Roshan', 51), 
#                              ('Ajay Devgn', 56), 
#                              ('Akshay Kumar', 57), 
#                              ('Shah Rukh Khan', 59), 
#                              ('Salman Khan', 59), 
#                              ('Aamir Khan', 60), 
#                              ('Amitabh Bachchan', 82)]

'''
# Key Points (Solution)
- Uses sorted() to order a list of tuples.
- Lambda function extracts age from each tuple (x[1]).
- key= argument tells sorted() what value to sort by.
- Sorting is done in ascending order by default.
- Original list remains unchanged (sorted() returns a new list).
-Also remember, sorted returns a list, so no type casting needed.
- Lambda keeps the sorting logic short and focused.

# Key Points (Output)
- Output is a list of (name, age) tuples.
- Tuples are ordered by age from youngest to oldest.
- Relative order is stable for equal ages.
- Example output starts with: ('Kartik Aaryan', 34)

# Important Note
- Always use key= when sorting complex structures.
- Lambdas are ideal for simple key-extraction logic.
'''
