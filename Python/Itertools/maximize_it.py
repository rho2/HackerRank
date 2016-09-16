from itertools import product

k, m = map(int, input().split())
l = [list(map(int, input().split()))[1:] for i in range(k)]

ma = 0
for p in list(product(*l)):
    ma= max(ma, sum([x**2 for x in p])%m)

print(ma)
