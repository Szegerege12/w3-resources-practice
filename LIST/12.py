""" Write a Python program to print a specified list after removing the
 0th, 4th and 5th elements.
 Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
 Expected Output : ['Green', 'White', 'Black']
"""

colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors = [x for (i,x) in enumerate(colors) if i not in (0,4,5)]
print(colors)