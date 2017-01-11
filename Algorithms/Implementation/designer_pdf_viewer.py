import string

h = list(map(int, input().split()))
word = input()

d = dict(zip(string.ascii_lowercase, h))
v = [d[c] for c in word]

w = max(v) * len(word)

print(w)