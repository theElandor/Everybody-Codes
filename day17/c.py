import sys
from collections import deque
filename = sys.argv[1]
# brilliant -> connections must be at least 6
# can have a forest of trees
# must find 3 largest trees
def dist(source, dest):
    x1,y1 = source
    x2,y2 = dest
    return abs(x1-x2) + abs(y1-y2)
with open(filename) as f:
    grid = f.read().splitlines()
    stars = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "*":
                stars.append((i,j))
    coords = set(stars)
    start = coords.pop()
    taken = [start]
    total = 0
    ans = []
    while coords:
        m = float("inf")
        for tx, ty in taken:# look in neighbor of each taken node
            for dx in range(-6, 6):
                for dy in range(-6, 6):
                    if (tx+dx,ty+dy) in coords:
                        d = dist((tx, ty), (tx+dx, ty+dy))
                        if d < m and d < 6:
                            source = (tx, ty)
                            dest = (tx+dx, ty+dy)
                            m = d
        if m == float("inf"):
            ans.append(total+len(taken))
            total =0
            start = coords.pop()
            taken = [start]
            continue
        taken.append(dest)
        coords.remove(dest)
        total += m
    ans.append(total+len(taken))    
    print(ans)
    final = sorted(ans, reverse=True)[:3]
    result = 1
    for f in final:
        result *= f
    print(final)
    print(result)
