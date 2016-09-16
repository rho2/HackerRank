from collections import deque
for _ in range(int(input())):
    t, c, stack = int(input()), deque(map(int, input().split())), []
    while c:
        if (stack[-1] >= max(c[0], c[-1]) if stack else 1):
            stack.append(c.pop() if c[-1] > c[0] else c.popleft())
        else:
            break
    print('No' if c else 'Yes')