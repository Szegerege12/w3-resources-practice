"""Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
Sample Data : Python 3.2
Expected Output :
Letters 6
Digits 2"""

word = str(input("Enter a string to calculate: "))
let = []
dig = []

for char in word:
    if char.isdigit():
        dig.append(char)
    elif char.isalpha():
        let.append(char)

print("Letters:", len(let))
print("Digits", len(dig))
