from itertools import combinations
_ = input()
n = input().strip().split()
k = int(input())

t = list(combinations(n,k))
print(len([s for s in t if 'a' in s])/len(t))