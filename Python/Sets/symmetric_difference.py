_ = input()
m = set(input().split())
_ = input()
n = set(input().split())

print('\n'.join(sorted(m.symmetric_difference(n),key=int)))