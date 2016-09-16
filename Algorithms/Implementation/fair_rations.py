n = int(input().strip())
b = map(int, input().strip().split())

sum = 0
c = False
for i in b:
    c = (c + i) % 2
    sum += c * 2

if c:
    print('NO')
else:
    print (sum)