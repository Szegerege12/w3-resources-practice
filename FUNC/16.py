"""Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included)."""


def squares_list():
    results = []
    for num in range(1,31):
        square = num * num
        results.append(square)

    print(results)



squares_list()