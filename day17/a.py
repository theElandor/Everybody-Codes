import sys
from collections import deque
# just a minimum spanning tree
filename = sys.argv[1]
def dist(source, dest):
    x1,y1 = source
    x2,y2 = dest
    return abs(x1-x2) + abs(y1-y2)
with open(filename) as f:
    grid = f.read().splitlines()
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "*":
                coords.append((i,j))    
    taken = [coords[0]]
    coords = coords[1:]
    total = 0
    while coords:
        m = float("inf")
        for tx, ty in taken:
            for cx, cy in coords:
                if dist((tx, ty), (cx, cy)) < m:
                    source = (tx,ty)
                    dest = (cx,cy)
                    m = dist(source, dest)
        taken.append(dest)
        coords.remove(dest)
        total += m
    print(total+len(taken))
    

