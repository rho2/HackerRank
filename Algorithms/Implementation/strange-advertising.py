import math

n = int(input())
l = 0
a = 5

for i in range(n):
    l += math.floor(a/2)
    a = math.floor(a/2)*3
    

print(l)