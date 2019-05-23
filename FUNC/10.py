"""Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""

def even_from_list(list):
    result = []
    for num in list:
        if num % 2 == 0 :
            result.append(num)

    print(result)


even_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
