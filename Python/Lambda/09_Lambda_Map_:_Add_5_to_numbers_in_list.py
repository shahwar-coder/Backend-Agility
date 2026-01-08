'''
9. Given a list of numbers, use map() and lambda to add 5 to each number.
'''

def main()->None:
    try:
        numbers = [1,2,3,4,5]
        add_5_to_num = lambda x : x+5
        result = list(map(add_5_to_num, numbers))
        print(f"Numbers now: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__=="__main__":
    main()

# Numbers now: [6, 7, 8, 9, 10]