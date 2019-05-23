""" Write a Python program to add 'ing' at the end of a
given string (length should be at least 3). If the given string already
 ends with 'ing' then add 'ly' instead"""


def add_ing(string):
    if len(string) < 3:
        print(string)

    if string.endswith('ing'):
        newstring = string + 'ly'
    else:
        newstring = string + 'ing'

    return newstring


print(add_ing('string'))
