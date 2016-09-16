_, A = input(), set(input().split())

for _ in range(int(input())):
    getattr(A, input().split()[0])(set(input().split()))

print(sum(map(int,A)))