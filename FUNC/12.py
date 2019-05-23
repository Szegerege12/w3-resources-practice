"""Write a Python function that checks whether a passed string is palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
 e.g., madam or nurses run."""


def is_palindrome(word):
    if word == word[::-1]:
        print(word,'is palindrome')
    else:
        print(word,'its not palindrome')



is_palindrome('bubu')