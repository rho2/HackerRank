_ = input()

l = set(map(int, input().strip().split(' ')))
l.remove(max(l))

print(max(l))