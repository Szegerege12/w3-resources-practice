"""Write a Python function that takes a list and returns a new list with unique elements of the first list."""

def seg_list(list):
    uniq = []
    for element in list:
        if element in uniq:
            continue
        else:
            uniq.append(element)

    print(uniq)


seg_list([1,2,3,3,3,3,4,5])