for i in range(0,50):
    if i % 3 == 0 :
        print('fizz')
        continue
    elif (i % 3 ==0) and (i % 5 == 0):
        print('buzz')
        continue
    print(i)
