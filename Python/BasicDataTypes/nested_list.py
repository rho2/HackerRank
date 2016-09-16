l = [[input(), float(input())] for _ in range(int(input()))]

s = sorted(list(set([m for n, m in l])))[1]
print('\n'.join(sorted([a for a,b in l if b == s])))