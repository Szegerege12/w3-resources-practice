""" Write a Python program to get the frequency of the elements in a list"""

import collections

my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

print('Original list:', my_list)
ctr = collections.Counter(my_list)
print('Frequency:', ctr)