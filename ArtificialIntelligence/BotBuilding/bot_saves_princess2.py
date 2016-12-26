def nextMove(n,r,c,grid):
    for x in range(n):
        for y in range(n):
            if(grid[x][y] == 'p'):
                row, col = x,y
    if(col != c):
        return (col > c) and 'RIGHT' or 'LEFT'
    else:
        return (row > r) and 'DOWN' or 'UP'

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))