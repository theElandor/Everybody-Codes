import sys
filename = sys.argv[1]
rots = int(sys.argv[2])
def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, end="")
        print("")
        
def rotate(grid,rotations, x,y, reverse=False):
    temp = None
    rots = rotations if not reverse else rotations[::-1]
    for i, (k,v) in enumerate(rots):
        if not reverse:
            tx, ty = k
            sx, sy = v
        else:
            sx, sy = k
            tx, ty = v
        if not temp: temp = grid[x+tx][y+ty]
        if i ==  len(rotations)-1: grid[x+tx][y+ty] = temp
        else: grid[x+tx][y+ty] = grid[x+sx][y+sy]
            
with open(filename) as f:
    data = f.read().split("\n\n")
    ops = list(data[0])
    grid = [list(x) for x in data[1].splitlines()]
    t = [[(-1,-1),(-1,0)],
         [(-1,0),(-1,1)],
         [(-1,1),(0,1)],
         [(0,1),(1,1)],
         [(1,1),(1,0)],
         [(1,0),(1,-1)],
         [(1,-1),(0,-1)],
         [(0,-1),(-1,-1)]]
#    rotate(grid, t, 1,1,reverse=False)# counterclock -> left
#    print_grid(grid)
    m = len(grid)
    n = len(grid[0])
    for _ in range(rots):
        k = 0
        for i in range(1, m-1):
            for j in range(1,n-1):
                reverse = (ops[k] == "R")                
                rotate(grid, t, i,j, reverse)
                k = (k+1)%len(ops)
    print_grid(grid)
    # if any(["<" in row and ">" in row for row in grid]):
    #     print_grid(grid)
    #     exit(0)
