"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""


def count_string(items):
    """
    Zlicza slowa które mają wiecej niż dwa znaki oraz kończą się i zaczynają tą samą literą
    :param items:
    :return: count of words
    """
    count = 0
    for item in items:
        if len(item) > 2 and item[0] == item[-1]:
            count += 1

    return count


print(count_string(['abc', 'xzx', 'aba', '1221']))
