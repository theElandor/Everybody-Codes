import math
from collections import deque
directions = [(0,1,0),(1,0,0),(-1,0,0),(0,-1,0), (0,0,-1), (0,0,1)]
mapping = {
    "U": (1,0,0),
    "D": (-1,0,0),
    "R": (0,1,0),
    "L": (0,-1,0),
    "F": (0,0,1),
    "B": (0,0,-1)
}
def bfs(grid, x,y,z):
    # compute distance from (x,y,z) to all other nodes
    Q = deque()
    visited = set()
    dist = {}
    Q.append((x,y,z,0))
    visited.add((x,y,z))
    while Q:
#        print(Q)
        x,y,z,distance = Q.popleft()
        for dx, dy, dz in directions:
            # check if valid
            if (x+dx, y+dy, z+dz) in grid and (x+dx, y+dy, z+dz) not in visited:
                Q.append((x+dx, y+dy, z+dz, distance+1))
                dist[(x+dx, y+dy, z+dz)] = distance+1
                visited.add((x+dx, y+dy, z+dz))
    return dist
        

with open("input3.txt") as f:
    branches = [x.split(",") for x in f.read().splitlines()]
    grid = set()
    leaves = set()
    trunk = []
    for b in branches:
        current = (0,0,0)
        for i,c in enumerate(b):
            d,n = c[0], int(c[1:])
            dx,dy,dz = mapping[d]
            for step in range(n):
                x,y,z = current
                if current[0] != 0 and current[1] == 0 and current[2]==0:
                    trunk.append((x, y, z))
                grid.add((x+dx, y+dy, z+dz))
                current = (x+dx, y+dy, z+dz)
            if i == len(b)-1:
                leaves.add(current)
    ans = []
    for x,y,z in trunk:
        distances = bfs(grid,x,y,z)
        ans.append(sum([distances[(lx,ly,lz)] for lx,ly,lz in leaves]))
    print(min(ans))
