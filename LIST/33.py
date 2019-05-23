"""Write a Python program to generate all sublists of a list."""


def sub_lists(list1):
    sublists = [[]]
    for i in range(len(list1) + 1):
        for j in range(i + 1, len(list1) + 1):
            sub = list1[i:j]
            sublists.append(sub)

    return sublists


list1 = [1, 2, 3, 4, 5]
print(sub_lists(list1))
