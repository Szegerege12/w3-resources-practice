"""Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself."""


def replace_char(string):
    char = string[0]
    string = string.replace(char, '$')
    string = char + string[1:]

    return string


print(replace_char('restart'))