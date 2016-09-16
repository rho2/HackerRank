from itertools import product

a = set(map(int, input().strip().split()))
b = set(map(int, input().strip().split()))

print(' '.join(map(str, product(a, b))))