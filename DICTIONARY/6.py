"""Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x)
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


def make_a_dict(n):
    dict_n = {}
    for n in range(1, n+1):
        dict_n[n] = n * n

    return print(dict_n)


make_a_dict(5)
