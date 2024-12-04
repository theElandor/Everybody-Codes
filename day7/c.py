import sys
directions = [(-1,0),(0,-1),(0,1),(1,0)]
def ok(x,y,grid):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    return True

filename = sys.argv[1]
grid = [list(x) for x in open("track2.txt").read().splitlines()]
current = (0,0)
visited = set()
visited.add((0,0))
track = ""
while True:
    x,y = current
    track += grid[x][y]
    for dx, dy in directions:
        if(x+dx, y+dy) in visited: continue
        if ok(x+dx, y+dy, grid) and grid[x+dx][y+dy] != " ":
            current=(x+dx, y+dy)
            visited.add((x+dx, y+dy))
            break
    if current == (0,0):
        break
print(track)
# 5+, 3-, 3= is valid
# 2024 loops