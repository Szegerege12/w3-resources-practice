"""Write a Python program which accepts a sequence of comma separated
  4 digit binary numbers as its input and print the numbers that are divisible
  by 5 in a comma separated sequence
  Sample Data : 0100,0011,1010,1001,1100,1001
  Expected Output : 1010
  """
list = []
data = input("Please enter sequence of digits 1/0 separated by comma"
                 "for example(0111,0001,1000):")
num = data.split(',')

for number in num:
    list.append(number)



for number in list:
    if int(number) % 5 == 0:
        print(number)