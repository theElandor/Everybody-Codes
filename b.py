import sys
from collections import deque
filename = sys.argv[1]
directions = [(1,0), (0,1), (-1,0), (0,-1)]
def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, end="")
        print("")
with open(filename) as f:
    grid = [list(x) for x in f.read().splitlines()]
    palms = set()
    stones = set()
    starts = []
    m = len(grid)
    n = len(grid[0])
    for i in range(len(grid)):
        if grid[i][0] == ".":
            starts.append((i,0))
        if grid[i][n-1] == ".":
            starts.append((i,n-1))
        for j in range(len(grid[0])):            
            if grid[i][j] == "P":
                palms.add((i,j))
            elif grid[i][j] == "#":
                stones.add((i,j))                
    Q = deque(starts)
    visited = set()
    time = 0
    qlen = 1
    while Q:
        x, y = Q.popleft()
        qlen -= 1        
        for dx, dy in directions:
            if x+dx in range(m) and y+dy in range(n):
                if (x+dx, y+dy) in visited:continue
                if (x+dx, y+dy) not in stones:
                   Q.append((x+dx, y+dy))
                   visited.add((x+dx, y+dy))
                   if (x+dx, y+dy) in palms:
                       palms.remove((x+dx, y+dy))
        if qlen == 0:
            time += 1
            qlen = len(Q)
        if not palms:
            break
    print(time-1)
