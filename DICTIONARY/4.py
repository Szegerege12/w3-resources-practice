"""Write a Python program to check if a given key already exists in a dictionary."""

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_in_dict(x):
    if x in d:
        print('Key', x, 'is present in the dictionary')
    else:
        print('Key', x, 'is not present in the disctionary')


is_key_in_dict(8)