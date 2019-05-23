"""Write a Python program to remove duplicates from a list."""

a = [10,20,30,20,10,50,60,40,80,50,40]

duplicated = set() # set zapewnia że w nim nie będzie duplikatów
uniq_items = []
for x in a:
    if x not in duplicated:
        uniq_items.append(x)
        duplicated.add(x)

print(uniq_items)
print('duplikaty:', duplicated)