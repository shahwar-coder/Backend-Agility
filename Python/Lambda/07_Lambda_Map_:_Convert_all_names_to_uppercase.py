'''
7. Given a list of names, use map() and lambda to convert all names to uppercase.
'''

def main()->None:
    try:
        names = ["rahul gandhi", "sonia gandhi", "priyanka gandhi", "shahwar alam"]
        names_to_upper_case = lambda x : x.upper()
        result = list(map(names_to_upper_case, names))
        print(f"Names after uppercase: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Names after uppercase: ['RAHUL GANDHI', 'SONIA GANDHI', 'PRIYANKA GANDHI', 'SHAHWAR ALAM']