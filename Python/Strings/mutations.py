s = input()
a = input().split()

n = int(a[0])

print(s[:n] + a[1] + s[n+1:])