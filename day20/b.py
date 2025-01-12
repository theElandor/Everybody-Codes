import sys

filename = sys.argv[1]
directions = [(-1,0), (0,1), (1,0), (0,-1)] # N E S W
TL = 3000
# This one was really hard. I had to use dictionaries instead
# of queues to keep track of states, as they are faster then collections.deque.
# Had to check reddit for this hint anyway.
# The problem is not conceptually hard, but it requires good code performance
# as the state space is very big (5 numbers)

def find_start(grid:list) -> tuple:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                return (i,j)

with open(filename) as f:
    grid = [list(x) for x in f.read().splitlines()]
    m = len(grid)
    n = len(grid[0])
    start = find_start(grid)
    sx, sy = start
    ans = float("inf")
    states = {}
    for i in range(len(directions)):
        states[(TL, sx, sy, i, 0)] = 10000
    while True:
        new_states = {}
        for state, h in states.items():
#            print(state)
            t, x,y,i, check = state
            if t < 0: continue
            if grid[x][y] == "S" and h >= 10000 and check == 4:
                ans = min(ans, TL - t)
                print(ans)
                continue
            for di in (-1, 0, 1):
                nd = (i+di) % len(directions)
                dx, dy = directions[nd]
                if 0 <= x+dx < m  and 0 <= y+dy < n and grid[x+dx][y+dy] != "#":
                    nc = grid[x+dx][y+dy]
                    ns = (t-1, x+dx, y+dy, nd, check)
                    if nc == "+":                    
                        if ns not in new_states or new_states[ns] < h+1:
                            new_states[ns] = h+1
                    elif nc == "-":
                        if ns not in new_states or new_states[ns] < h-2:
                            new_states[ns] = h-2
                    elif nc == ".":
                        if ns not in new_states or new_states[ns] < h-1:
                            new_states[ns] = h-1
                    elif nc in ["A","B","C","S"]:
                        if nc == "A":
                            if check != 0: continue
                        elif nc == "B":
                            if check != 1: continue
                        elif nc == "C":
                            if check != 2: continue
                        elif nc == "S":
                            if check != 3: continue
                        ns = (t-1, x+dx, y+dy, nd, check+1)
                        if ns not in new_states or new_states[ns] < h-1:
                            new_states[ns] = h-1
        states = new_states
    print(f"ans: {ans}")
