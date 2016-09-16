from itertools import permutations
word, k = input().strip().split()
p = [''.join(a) for a in permutations(word, int(k))]


print('\n'.join(sorted(p)))