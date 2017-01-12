n, k = map(int, input().strip().split())
c = list(map(int, input().split()))
b = int(input().strip())

print((sum(c) - c[k])// 2 == b and 'Bon Appetit' or c[k] // 2)