n = input()

m = map(int, input().strip().split(' '))
t = tuple(m)
h = hash(t)

print(h)