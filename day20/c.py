import sys

filename = sys.argv[1]
with open(filename) as f:
    grid = [list(x) for x in f.read().splitlines()]
    m = len(grid)
    n = len(grid[0])
    start = (1,31)
    h = 384399
    x,y = start
    d = 1
    while True:
        if h == 0:
            break
        x = (x + 1)%m
        if grid[x][y] == "+": h += 1
        elif grid[x][y] == "-": h -= 2
        elif grid[x][y] == ".": h -= 1
        d += 1
    print(d)
    
