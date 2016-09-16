from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,input().split())

for i in range(1,n+1):
    d[input()].append(i) 

for i in range(0,m):
    list1 += [input()]  

for i in list1: 
    if i in d:
        print(" ".join( map(str,d[i]) ))
    else:
        print(-1)