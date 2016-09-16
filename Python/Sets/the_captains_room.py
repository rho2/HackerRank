k, g = int(input()), list(map(int,input().split()))

print(((sum(set(g))*k)-(sum(g)))//(k-1))