"""Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

# pierwszy sposob na piechote
dict_n = {}
#dict_n.update(dic1)
#dict_n.update(dic2)
#dict_n.update(dic3)
#print(dict_n)


for d in (dic1, dic2, dic3):
    dict_n.update(d)

print(dict_n)