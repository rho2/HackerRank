from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

for i in OrderedCounter(sorted(input())).most_common(3):
    print(' '.join(map(str, i)))
