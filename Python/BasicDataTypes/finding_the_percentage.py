l = {}
for _ in range(int(input())):
    s = input().split()
    l[s[0]] = sum([float(a) for a in s[1:]])/(len(s)-1)
    
print('%.2f' % l[input()])