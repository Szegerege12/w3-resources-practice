"""check is dictionary empty"""

a = {'a': 10, "b": 12, "c": 13}
b = {}


def is_empty(dictionary):
    if dictionary:
        print('Not empty')
    else:
        print('Its empty')


is_empty(a)
is_empty(b)
