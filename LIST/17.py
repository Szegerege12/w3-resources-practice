"""
Write a Python program to generate and print a list except for the first 5 elements,
 where the values are square of numbers between 1 and 30 (both included)
"""

def print_values():
    lista = []
    for element in range(5,25,1):
        lista.append(element ** 2)

    return print(lista)


print_values()