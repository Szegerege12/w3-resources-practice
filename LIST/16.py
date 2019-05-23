"""Write a Python program to generate and print a list of
 first and last 5 elements where the values are square of
 numbers between 1 and 30 (both included)."""


def print_values():
    lista = []
    for i in range(1, 6, 1):
        lista.append(i ** 2)
    for x in range(26, 31, 1):
        lista.append(x ** 2)
    print(lista)


print_values()