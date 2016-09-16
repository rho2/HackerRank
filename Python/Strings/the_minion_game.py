a = input()
v = 'AEIOU'
l = len(a)
k, s = 0,0

for i in range(l):
    if a[i] in v:
        k += (l-i)
    else:
        s += (l-i)

if k > s:
    print("Kevin", k)
elif k < s:
    print("Stuart", s)
else:
    print("Draw")