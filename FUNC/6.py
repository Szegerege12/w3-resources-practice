"""Write a Python function to check whether a number is in a given range."""


def test_in_range(n):
    if n in range(3,9):
        print( " %s in the range"%str(n))
    else:
        print("The number is not in the range")


test_in_range(5)