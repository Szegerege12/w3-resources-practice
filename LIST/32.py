"""Check whether a list contains a sublist"""


def checker(list, sublist):


    print('Original list:', list)
    print('Sublist:', sublist)
    flag = 0
    if (all(x in list for x in sublist)):
        flag = 1

    if flag:
        print('Its sublist')
    else:
        print('Its not')

checker([9, 4, 5, 8, 10], [10, 5, 4])
