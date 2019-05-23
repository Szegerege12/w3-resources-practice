import itertools

original = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


new = list(itertools.chain(*original))

print(new)
