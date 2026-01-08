'''
10. Using map() and lambda, extract the first character from each string in a list.
'''

def main() -> None:
    try:
        words = ["apple", "banana", "kiwi", "mango"]
        get_first_char = lambda x: x[0]
        result = list(map(get_first_char, words))
        print(f"First characters: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
