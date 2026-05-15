from tabulate import tabulate

data = [
    [1, "Rahul", 28],
    [2, "Amit", 35],
]

headers = ["id", "name", "age"]

print(tabulate(data, headers=headers))