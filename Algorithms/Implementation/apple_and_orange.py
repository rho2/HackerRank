s,t = map(int, input().split())
a,b = map(int, input().split())
m,n = map(int, input().split())

da = list(map(int, input().split()))
do = list(map(int, input().split()))

mda = s - a     # max distance for apples
mdo = b - t     # max distance for oranges

aoh = sum(s <= a + d <= t for d in da)
ooh = sum(s <= b + d <= t for d in do)

print(aoh)
print(ooh)