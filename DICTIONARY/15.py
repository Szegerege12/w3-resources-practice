import operator

stats = {'a':1000, 'b':3000, 'c': 100, 'd': 90000}

maksimum = max(stats.items(), key=operator.itemgetter(1))
minimum = min(stats.items(), key=operator.itemgetter(1))
print('Smallest value:',minimum)
print('Biggest value:',maksimum)