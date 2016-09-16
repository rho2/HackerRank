from collections import OrderedDict
o = OrderedDict()
for i in range(int(input())):
    a = input().strip().split()
    n = ' '.join(a[:-1])
    if n in o:
        o[n] += int(a[-1])
    else:
        o[n] = int(a[-1])

for i in o.items():
    print(*i)