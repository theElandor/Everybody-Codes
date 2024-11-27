from heapq import heappop, heappush
import math

ans = []
directions = [(0,1),(1,0),(-1,0),(0,-1)]
# slow dfs
def explore(x,y,grid,count,visited,end):
    if (x,y) == end:
        ans.append(count)
        return
    current = int(grid[x][y])
    for dx, dy in directions:
        if x+dx >= 0 and x+dx < len(grid) and y+dy >= 0 and y+dy < len(grid[0]):
            if (x+dx, y+dy) in visited:
                continue
            target = grid[x+dx][y+dy]
            if target != "#":
                target = int(target)
                newcount = count + abs(target-current) +1 
                visited.add((x+dx, y+dy))
                explore(x+dx, y+dy, grid, newcount, visited, end)
                visited.remove((x+dx, y+dy))

def dij(grid, start, end, others):
    cant = set(others)
    dist = {}
    ans = {}
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            dist[(i,j)] = math.inf
            ans[(i,j)] = -1
    dist[start] = 0
    Q = [(0, start)]
    while Q:
        distance, u = heappop(Q)
        x,y = u
        if ans[u] != -1: continue
        ans[u] = distance
        # iterate on neighs
        for dx, dy in directions:
            if x+dx >=0 and x+dx < len(grid) and y+dy >= 0 and y+dy < len(grid[0]):
                target = grid[x+dx][y+dy]
                if target == "#":
                    continue
                if (x+dx, y+dy) in cant:
                    continue
                diff = abs(int(target)-int(grid[x][y]))
                current_distance = min(diff, 10-diff)
                alt = distance + current_distance + 1
                heappush(Q,(alt,(x+dx, y+dy)))
    if ans[end] != -1:
        return ans[end]
    else:
        return math.inf

with open("input3.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]
    starts = []
    for i,row in enumerate(grid):
        for j,el in enumerate(row):
            if el == "S":
                starts.append((i,j)) 
            elif el == "E":
                end = (i,j)
            elif el == " ":
                grid[i][j] = "#"
    ei, ej = end
    print(starts)
    for si,sj in starts:
        grid[si][sj] = 0
    grid[ei][ej] = 0
    result = math.inf
    for start in starts:
        print(result)
        result = min(result, dij(grid, start, end, starts))
    print(result)
