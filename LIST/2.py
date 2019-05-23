"Write a Python program to multiplies all the items in a list."


def multiply_list(items):
    total = 1
    for x in items:
        total *= x
    return total

print(multiply_list([1,1,4]))