"""Write a Python program to count the number of even and odd numbers from a series of numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        odd.append(num)
    else:
        even.append(num)

print("Even numbers:",len(even))
print("Odd numbers:",len(odd))