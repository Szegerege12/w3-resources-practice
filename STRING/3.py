"Write a Python program to get a string made of the first 2 and the last 2"
"chars from a given a string. If the string length is less than 2, return instead of the empty string"


def create_string(string):
    if len(string) < 2 :
        return ''

    word = string[0:2] + string[-2:]
    print(word)



create_string('w')