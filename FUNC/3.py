

def multi(numbers):
    result = 1
    for x in numbers:
        result *= x

    return result


print(multi((8, 2, 3, -1, 7)))