'''
13. Using filter() and lambda, extract numbers greater than 50 from a list.
'''

def main() -> None:
    try:
        numbers = [10, 25, 60, 45, 80, 30, 90]
        greater_than_50 = lambda x: x > 50
        result = list(filter(greater_than_50, numbers))
        print(f"Numbers greater than 50: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()

# Numbers greater than 50: [60, 80, 90]