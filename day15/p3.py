# This problem took me more than it should. The idea is that the 3 "columns"
# of the input are connected by just a little passage on the bottom left / bottom right.
# The idea is to compute the route to collect also E and R, then compute the routes
# for the left and right columns without wanting to pick E and R as they have alredy been picked.
# Code looks like shit, should refactor it someday. :/
from collections import deque
from copy import deepcopy
from heapq import heappop, heappush
import sys
directions = [(1,0),(0,1),(-1,0),(0,-1)]

def valid(grid, position):
    x,y,distance = position
    m = len(grid)
    n = len(grid[0])
    if x >= 0 and x < m and y >= 0 and y < n:
        return True
    return False

def bfs(grid, start, kinds, solutions):
    dist = {}
    Q = [start]
    visited = set()
    distance, x,y, coll = start
    visited.add((x,y, frozenset(coll)))
    while Q:
        distance, x,y,coll = heappop(Q)
        for dx,dy in directions:
            v = x+dx, y+dy, distance+1
            if valid(grid, v) and grid[x+dx][y+dy] not in  "# ~".split() and (x+dx, y+dy, frozenset(coll)) not in visited:
                ncoll = deepcopy(coll)
                if grid[x+dx][y+dy] != ".":
                    ncoll.add(grid[x+dx][y+dy])
                    if len(ncoll) == kinds:
                        solutions.append((x+dx, y+dy, distance+1))                        
                heappush(Q, (distance+1, x+dx, y+dy, ncoll))
                visited.add((x+dx, y+dy, frozenset(ncoll)))
                dist[(x+dx),(y+dy)] = distance+1
    return dist,solutions

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
def find_herbs(grid):
    herbs = {}
    for i,row in enumerate(grid):
        for j, el in enumerate(row):
            if el not in "# ~ .".split():
                if el not in herbs: herbs[el] = [(i,j)]
                else: herbs[el].append((i,j))
    return herbs

def compute(grid, sx, sy):
    solutions = []
    backwards = simple_bfs(grid, (sx,sy,0))
    herbs = find_herbs(grid)
    if sx != 0:
        grid[sx][sy] = "."
        for x in "E R".split():
            if x in herbs: del herbs[x]
    print(herbs.keys())
    start = (0,sx,sy,set())
    bfs(grid, start, len(herbs.items()), solutions)
    finals = [backwards[(x,y)]+z for x,y,z in solutions]
    return (min(finals))
def find_start(row, element, reverse=False):
    found = []
    for i, x in enumerate(row):
        if x == element:
            if reverse: return i
            else: found.append(i)
    return found[-1]

def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, end="")
        print("")

if len(sys.argv) != 2:
    print("Provide input file")
    exit(0)
infile = sys.argv[1]
with open(infile) as f:
    grid = [list(x) for x in f.read().splitlines()]
    grid1 = [x[0:84] for x in grid]
    grid2 = [x[83:172] for x in grid]
    grid3 = [x[171:] for x in grid]

    middle = compute(grid2, 0, grid2[0].index("."))
    
    left_start = find_start(grid1[-2], "E")
    left = compute(grid1, len(grid1)-2, left_start)
    
    right_start = find_start(grid3[-2], "R", reverse=True)
    right = compute(grid3, len(grid3)-2, right_start)
    print(middle + left + right)
