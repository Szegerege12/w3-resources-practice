""" Write a Python function to check whether a string is a pangram or not. Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog" """


import string, sys
def is_panagram(string, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(string.lower())

print(is_panagram('The quick brown fox jumps over the lazy dog'))