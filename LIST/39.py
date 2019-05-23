"""Write a Python program to convert a list of multiple integers into a single integer
Sample list: [11, 33, 50]
Expected Output: 113350
"""

# 1 way
list1 = [11, 33, 50]

s = [str(i) for i in list1]

res = int("".join(s))

print(res)

# 2 way

for i in list1:
    print(i,end="")