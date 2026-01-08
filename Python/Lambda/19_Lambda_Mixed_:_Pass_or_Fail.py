'''
19. Use map() and lambda to convert a list of integers into
"Pass" if number ≥ 40, otherwise "Fail".
'''

def main() -> None:
    try:
        marks = [25, 40, 55, 30, 75, 38, 90]
        pass_or_fail = lambda x: "Pass" if x >= 40 else "Fail"
        result = list(map(pass_or_fail, marks))
        print(f"Result: {result}")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
