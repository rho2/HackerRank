n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = [ all(i % y == 0 for y in a) & all(x % i == 0 for x in b) for i in range(max(a),min(b)+1)]
print(sum(l))