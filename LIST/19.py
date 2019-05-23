"""Write a Python program to get the difference between the two lists.
"""

colors1 = ['red', 'blue', 'orange', 'green']
colors2 = ['red', 'orange']

diff = list(set(colors1) - set(colors2))

print(diff)