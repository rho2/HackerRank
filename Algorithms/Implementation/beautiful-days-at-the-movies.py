i,j,k = map(int, input().split())
s = sum([(i - int(str(i)[::-1])) % k == 0 for i in range(i,j+1)])

print(s)