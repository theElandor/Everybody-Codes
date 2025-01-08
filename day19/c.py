import sys
import os
from copy import deepcopy
#import graphviz
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
        
def get_loop_values(grid, loop):
    r = []
    for x,y  in loop:
        r.append(grid[x][y])
    return tuple(r)

def perform_loop(grid, loop):
    si,sj = loop[0]
    prev = grid[si][sj]
    for i in range(1,len(loop)):
        ti,tj = loop[i]
        current = grid[ti][tj]
        grid[ti][tj] = prev
        prev = current
        # copy temp in next
    grid[si][sj] = prev
            
with open(filename) as f:
    data = f.read().split("\n\n")
    ops = list(data[0])
    grid_ = [list(x) for x in data[1].splitlines()]
    grid = [[] for _ in range(len(grid_))]
    for i in range(len(grid_)):
        for j in range(len(grid_[0])):
            current = grid_[i][j]
            grid[i].append((i,j,current))
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
    state = None
    k = 0
    for i in range(1, m-1):
        for j in range(1,n-1):
            reverse = (ops[k] == "R")                
            rotate(grid, t, i,j, reverse)
            k = (k+1)%len(ops)
#    print_grid(grid)
    moves = {}
    for i in range(m):
        for j in range(n):
            oi, oj, val = grid[i][j]            
            moves[(oi,oj)] = (i,j)
    loops = []
    s = set()
    for i in range(m):
        for j in range(n):
            s.add((i,j))
    while s:
        current = s.pop()
        start = current
        l = [current]        
        while True:
            target = moves[current]
            if target == start: break
            l.append(target)
            s.remove(target)
            current = target
        if len(l) != 1:
            loops.append(l)
    for loop in loops:
        seen = {}
        for current in range(1,100000000000):
            perform_loop(grid_, loop)
            r = get_loop_values(grid_, loop)
            if r not in seen: seen[r] = current
            else:
                cycle = current - seen[r]
                loops_done = current
                break
        left_todo = (rots - loops_done) % cycle
        for _ in range(left_todo):
            perform_loop(grid_, loop)
    print_grid(grid_)
# 1324728834511171 # -> prev decoded
# 1048576000 # -> new number of ops

