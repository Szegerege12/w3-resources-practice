""" Write a Python program to get unique values from a list."""


def unique(list1):

    list_set = set(list1)

    unique_list = (list(list_set))
    for x in unique_list:
        print(x)

list1 = [10, 20, 10, 30, 40, 40]
unique(list1)