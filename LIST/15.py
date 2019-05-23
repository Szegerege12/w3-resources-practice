"""Write a Python program to shuffle and print a specified list."""
import random


def list_shuffle(list):
    random.shuffle(list)
    return print("List after shuffle:", list)


list_shuffle([1,23,1324,436,324,213,34,65,213,123,8435,22])