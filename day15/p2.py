# must find shortest path to collect 1 plant of each kind
from collections import deque
from copy import deepcopy
directions = [(1,0),(0,1),(-1,0),(0,-1)]
solutions = []
def valid(grid, position):
    x,y,distance = position
    m = len(grid)
    n = len(grid[0])
    if x >= 0 and x < m and y >= 0 and y < n:
        return True
    return False
def bfs(grid, start, kinds):
    dist = {}
    Q = deque()
    Q.append(start)
    visited = set()
    x,y,distance, coll = start
    visited.add((x,y, frozenset(coll)))
    while Q:
        x,y,distance,coll = Q.popleft()
        for dx,dy in directions:
            v = x+dx, y+dy, distance+1
            if valid(grid, v) and grid[x+dx][y+dy] not in  "# ~".split() and (x+dx, y+dy, frozenset(coll)) not in visited:
                ncoll = deepcopy(coll)
                if grid[x+dx][y+dy] != ".":
                    ncoll.add(grid[x+dx][y+dy])
                    if len(ncoll) == kinds:
                        print(ncoll)
                        solutions.append((x+dx, y+dy, distance+1))
                Q.append((x+dx, y+dy, distance+1, ncoll))
                visited.add((x+dx, y+dy, frozenset(ncoll)))
                dist[(x+dx),(y+dy)] = distance+1
    return dist

def simple_bfs(grid, start):
    dist = {}
    Q = deque()
    Q.append(start)
    visited = set()
    x,y,distance = start
    visited.add((x,y))
    while Q:
        x,y,distance = Q.popleft()
        for dx,dy in directions:
            v = x+dx, y+dy, distance+1
            if valid(grid, v) and grid[x+dx][y+dy] not in "# ~".split() and (x+dx, y+dy) not in visited:
                Q.append(v)
                visited.add((x+dx, y+dy))
                dist[(x+dx),(y+dy)] = distance+1
    return dist    

with open("input2.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]
    herbs = {}
    for i,row in enumerate(grid):
        for j, el in enumerate(row):            
            if el not in "# ~ .".split():
                if el not in herbs: herbs[el] = [(i,j)]
                else: herbs[el].append((i,j))
    kinds = len(herbs.items())
    start = (0,grid[0].index("."),0, set())
    bfs(grid, start, kinds)
    start = (0,grid[0].index("."),0)
    backwards = simple_bfs(grid, start)
#    print(backwards[(6,8)])
    print(solutions)
    finals = [backwards[(x,y)]+z for x,y,z in solutions]
    print(finals)
    print(min(finals))
