"Write a Python program to count the number of characters (character frequency) in a string."

def char_frequency(str1):
    dict = {}
    for char in str1:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


print(char_frequency('google.com'))