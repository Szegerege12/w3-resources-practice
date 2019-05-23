list1 = [1, 23, 34, 54, 213, 2, 6]
list2 = [1, 23, 4, 2, 3, 5]

common = []
for x in list1:
    for y in list2:
        if x == y:
            common.append(x)


print(common)

