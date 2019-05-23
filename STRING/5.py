""" Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string"""


def single_string(str1, str2):
    chars1 = str1[0:2]
    chars2 = str2[0:2]

    new = chars2 + str1[2:] + " " + chars1 + str2[2:]
    return new


print(single_string('abc', 'xyz'))
