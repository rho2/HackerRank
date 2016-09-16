from collections import Counter
X, shoes = input(), Counter(map(int, input().strip().split()))

e = 0
for i in range(int(input())):
    s, p = map(int, input().split())
    if(shoes[s] > 0):
        e += p
        shoes[s] -= 1

print(e)