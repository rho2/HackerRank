from itertools import combinations
word, k = input().strip().split()
word = ''.join(sorted(word))

for i in range(int(k)):
    a = [''.join(b) for b in combinations(word,i+1)]
    print('\n'.join(a))