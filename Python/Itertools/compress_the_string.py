from itertools import groupby

s = input()
b = [list(g) for k, g in groupby(s)]
c = ['({1}, {0})'.format(a[0], len(a)) for a in b]

print(' '.join(c))