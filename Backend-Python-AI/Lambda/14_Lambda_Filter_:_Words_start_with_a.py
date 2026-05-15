'''
14. Given a list of words, use filter() and lambda to keep only words
that start with the letter 'a'.
'''

def main() -> None:
    try:
        words = ["apple", "banana", "apricot", "mango", "avocado", "kiwi"]
        starts_with_a = lambda x: x.startswith("a")
        result = list(filter(starts_with_a, words))
        print(f"Words starting with 'a': {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

# Words starting with 'a': ['apple', 'apricot', 'avocado']