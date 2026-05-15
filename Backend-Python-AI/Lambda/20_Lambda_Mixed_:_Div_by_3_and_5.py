'''
20. Given a list of numbers, use filter() and lambda to select
numbers divisible by both 3 and 5.
'''

def main() -> None:
    try:
        numbers = [5, 10, 15, 20, 30, 45, 60, 75, 90]
        divisible_by_3_and_5 = lambda x: x % 3 == 0 and x % 5 == 0
        result = list(filter(divisible_by_3_and_5, numbers))
        print(f"Numbers divisible by both 3 and 5: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
