import sys
from collections import deque
from copy import deepcopy
filename = sys.argv[1]
directions = [(1,0), (0,1), (-1,0), (0,-1)]
def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, end="")
        print("")
with open(filename) as f:
    grid = [list(x) for x in f.read().splitlines()]
    palms_ = set()
    stones = set()
    starts = []
    m = len(grid)
    n = len(grid[0])
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                starts.append((i,j))
            if grid[i][j] == "P":
                palms_.add((i,j))
            elif grid[i][j] == "#":
                stones.add((i,j))
    res = []
    for start in starts:
        palms = deepcopy(palms_)        
        Q = deque([start])
        visited = set()
        time = 0
        qlen = 1
        total = 0
        p_removed = 0
        print(start)
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
                           p_removed += 1
            if qlen == 0:
                time += 1
                qlen = len(Q)
                if p_removed: total += (p_removed * time)
                p_removed = 0
            if qlen == 0 and not palms:
                break
        res.append((total, start))
    print(sorted(res, key=lambda x:x[0])[0])
