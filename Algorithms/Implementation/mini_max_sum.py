X = list(map(int, input().split()))

X.sort()

l = sum(X[:4])
h = sum(X[1:])

print(str(l) + ' ' + str(h))
