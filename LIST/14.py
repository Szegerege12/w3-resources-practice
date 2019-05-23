"""Write a Python program to print the numbers of a specified list
after removing even numbers from it"""


list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
new = []
for x in list:
    if x%2 != 0:
        new.append(x)

print(new)
