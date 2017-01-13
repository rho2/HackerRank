from collections import Counter

n = int(input())
s = Counter(input().split())

print(sum(i//2 for i in s.values()))