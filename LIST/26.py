"""Write a python program to check whether two lists are circularly identical"""


def is_identical(list1, list2):
    if list1 == list2:
        print("Lists are identic")
    else:
        print("Lists are not equal")


is_identical([1,2,3], [1,2,2])