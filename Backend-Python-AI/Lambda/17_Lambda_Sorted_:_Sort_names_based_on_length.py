'''
17. Sort a (name, age) list of tuples, based on their length of names using sorted() and lambda.
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

        length_key = lambda x: len(x[0]) 
        result = sorted(indian_actors, key=length_key)
        print(f"Indian actors sorted by Length of their names: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

# Indian actors sorted by length of their names:
# [
#     ('Aamir Khan', 60),
#     ('Ajay Devgn', 56),
#     ('Salman Khan', 59),
#     ('Akshay Kumar', 57),
#     ('Ranbir Kapoor', 42),
#     ('Ranveer Singh', 39),
#     ('Kartik Aaryan', 34),
#     ('Shah Rukh Khan', 59),
#     ('Hrithik Roshan', 51),
#     ('Amitabh Bachchan', 82)
# ]


'''
# Key Points (Solution)
- Uses sorted() to sort a list of (name, age) tuples.
- Lambda function extracts the name and computes its length.
- key= argument directs sorted() to sort by name length.
- Sorting is ascending by default (shorter names first).
- Original list is not modified; a new sorted list is returned.
- Lambda keeps key logic concise and readable.

# Key Points (Output)
- Output is a list of (name, age) tuples.
- Tuples are ordered by increasing length of names.
- Stable sorting preserves relative order for equal lengths.
- Example output starts with: ('Aamir Khan', 60)

# Important Note
- key= is essential when sorting by derived values.
- Lambdas are ideal for simple, one-line key functions.
'''
