"""Write a Python function that takes a number as a parameter and check the number is prime or not
"""


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            print("Not prime number")
            break
        else:
            print("Prime number")
            break


is_prime(11)