from collections import deque
directions = [(1,0),(0,1),(-1,0),(0,-1)]
def valid(grid, position):
    x,y,distance = position
    m = len(grid)
    n = len(grid[0])
    if x >= 0 and x < m and y >= 0 and y < n:
        return True
    return False

def bfs(grid, start):
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
            if valid(grid, v) and grid[x+dx][y+dy] != "#" and (x+dx, y+dy) not in visited:
                Q.append(v)
                visited.add((x+dx, y+dy))
                dist[(x+dx),(y+dy)] = distance+1
    return dist


with open("input1.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]
    start = grid[0].index(".")
    herbs = []
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "H":
                herbs.append((i,j))
    entry = (0, start, 0)
    f_dist = bfs(grid, entry)
    forwards = [f_dist[x] for x in herbs]
    s_herbs = [(x,y,0) for x,y in herbs]
    b_dists = [bfs(grid, h) for h in s_herbs]
    sx,sy, d = entry
    backwards = [d[(sx,sy)] for d in b_dists]
    for f,b in zip(forwards, backwards):
        print(f"{f} + {b} = {f+b}")

    
    
