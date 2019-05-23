""" Write a Python program to find the list of words that are longer
 than n from a given list of words."""

words = ['dog', 'cat', 'motocykl', 'traktor', 'biblioteka']


def find_list(n, list):
    new = []
    for element in list:
        if len(element) > n:
            new.append(element)
    return new


print(find_list(3, words))
