'''
12. Given a list of strings, use filter() and lambda to keep only strings longer than 4 characters.
'''

def main()->None:
    try:
        words = ["shahwar", "alam", "naqvi", "shahrukh", "khan"]
        chars_greater_4 = lambda x : len(x)>4
        result = list(filter(chars_greater_4, words))
        print(f"Words with more than 4 chars : {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Words with more than 4 chars : ['shahwar', 'naqvi', 'shahrukh']