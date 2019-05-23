"""Write a Python function that accepts a string and calculate
 the number of upper case letters and lower case letters."""


def calculate_cases(string):
    upper = 0
    lower = 0
    for char in string:
        if char.islower() and char.isalpha():
            lower += 1
        elif char.isupper() and char.isalpha():
            upper += 1


    print("Lower count:", +lower)
    print("Upper count:", +upper)


calculate_cases('The quick Brow Fox')