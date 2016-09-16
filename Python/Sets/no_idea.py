n, m = input().split()
i = input().split()
a = set(input().strip().split())
b = set(input().strip().split())

print(sum([1 if x in a else -1 if x in b else 0 for x in i]))