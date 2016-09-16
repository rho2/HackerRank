from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input().strip())
print(sum(map(float,[Student(*input().strip().split()).MARKS for a in range(n)])) /n) 
