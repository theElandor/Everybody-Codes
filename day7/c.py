import sys
import time
paths = []
directions = [(-1,0),(0,-1),(0,1),(1,0)]

def gen_paths(p,m,e, current="") -> list:
    prev = current
    if p == 0 and m == 0 and e == 0:
        paths.append(current)
    if p > 0:
        current += "+"
        gen_paths(p-1, m, e, current)
        current = prev
    if m > 0:
        current += "-"
        gen_paths(p, m-1, e, current)
        current = prev
    if e > 0:
        current += "="
        gen_paths(p, m, e-1, current)

def print_grid(grid):
    for i,row in enumerate(grid):
        for j,el in enumerate(row):
            if el == " ":print("#", end="")
            else: print(el, end="")
        print("")

def race(track, plan, loops):
    fuel = 10
    total = 0
    i = 0
    d = {}
    for l in range(loops):
        p_i = i
        initial_fuel = fuel
        prev_total = total
        if i in d:
            delta, delta_fuel,ni = d[i]
            total += ((fuel * len(track)) + delta)
            fuel += delta_fuel
            i = ni
            continue 
        for el in track:            
            if el == "+": fuel+=1
            elif el == "-": fuel -= 1
            else:
                c = plan[i]
                if c == "+": fuel +=1
                elif c == "-": fuel -= 1
            total += fuel
            i = (i+1)%len(plan)
        delta = (total-prev_total) - (initial_fuel * len(track))
        if p_i not in d: d[p_i] = (delta,fuel - initial_fuel,i)
    return total
            
        
trackname = sys.argv[1]
loops = int(sys.argv[2])
grid = [list(x) for x in open(trackname).read().splitlines()]
current = (0,0)
visited = set([(0,0)])
track = ""
m = len(grid)
n = len(grid[0])

for r in grid:
    if len(r) != 71:
        for _ in range(71 - len(r)):
            r.append(" ")
while True:
    x,y = current
    track += grid[x][y]
    print(x,y)
    for dx, dy in directions:
        if(x+dx, y+dy) in visited: continue
        if x+dx in range(m) and y+dy in range(n) and grid[x+dx][y+dy] != " ":
            current=(x+dx, y+dy)
            visited.add((x+dx, y+dy))
            break
    if current == (1,0):
        x,y = current
        track += grid[x][y]
        break
track = track[1:]+"S"
target_plan = "-,-,+,+,=,=,+,=,+,-,+"
test_plan = "+,-,=,="
target = race(track, target_plan.split(","), loops)
print(target)
gen_paths(5,3,3)
counter = 0
for i,p in enumerate(paths):
    if i % 100 == 0: print(i)
    if race(track, list(p), loops) > target: counter += 1
print(counter)
