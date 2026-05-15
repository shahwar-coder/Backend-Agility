'''
15. Use filter() and lambda to remove empty strings from a list.
'''

def main() -> None:
    try:
        words = ["apple", "", "apricot", "", "avocado", ""]
        no_empty_strings = lambda x: len(x)
        result = list(filter(no_empty_strings, words))
        print(f"List of words (empty strings removed): {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

# List of words (empty strings removed): ['apple', 'apricot', 'avocado']

# for clarity if it confuses someone, you can use len(x) > 0
# or bool(x)