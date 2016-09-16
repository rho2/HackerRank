from itertools import combinations_with_replacement
word, k = input().strip().split()
word = ''.join(sorted(word))
p = [''.join(a) for a in combinations_with_replacement(word, int(k))]

print('\n'.join(sorted(p)))