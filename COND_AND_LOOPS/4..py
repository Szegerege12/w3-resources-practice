"""Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*"""

n = 5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

