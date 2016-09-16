from collections import OrderedDict
o = OrderedDict()
for i in range(int(input())):
    n = input().strip()
    if n in o:
        o[n] += 1
    else:
        o[n] = 1

print(len(o.items()))
print(' '.join(map(str, [v for i,v in o.items()])))