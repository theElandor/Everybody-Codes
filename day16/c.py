from copy import deepcopy
import sys
# stupid recursion + memoization
# can try to do this with standard DP
cache = {}
def get_coins(s:str) -> int:
    c = {x:s.count(x) for x in s}
    total =0
    for k, v in c.items():
        if v >= 3:
            total += 1 + (v-3)
    return total

def get_coins(s:str) -> int:
    c = {x:s.count(x) for x in s}
    total =0
    for k, v in c.items():
        if v >= 3:
            total += 1 + (v-3)
    return total

def state_to_coins(positions, wheels):
    state = tuple(positions)
    faces = []
    for i, w in enumerate(wheels):
        faces.append(w[state[i]])
    return get_coins("".join([x[0]+x[2] for x in faces]))

    
def spin(positions,wheels) -> list:
    temp = deepcopy(positions)
    for i in range(len(temp)):
        temp[i] = (temp[i]+numbers[i])%len(wheels[i])
    return state_to_coins(temp, wheels), temp

def left(positions, delta=1):
    temp = deepcopy(positions)
    for i in range(len(temp)):
        temp[i] = (temp[i]+delta)%len(wheels[i])
    return temp

def dp(positions, spins, wheels, mode=max) -> int:
    if spins == 0:
        return 0
    # do nothing
    if (tuple(positions), spins) in cache:
        return cache[(tuple(positions), spins)]
    c, np = spin(positions, wheels)
    o1 = c + dp(np,spins-1, wheels, mode=mode)
    # pull
    np = left(positions, delta=1)
    c,np = spin(np, wheels)
    o2 = c + dp(np,spins-1, wheels, mode=mode)
    # push
    np = left(positions, delta=-1)
    c,np = spin(np, wheels)
    o3 = c + dp(np,spins-1, wheels, mode=mode)
    result = mode([o1,o2,o3])
    cache[(tuple(positions), spins)] = result
    return result


filename = sys.argv[1]
with open(filename) as f:    
    stuff = f.read().split("\n\n")
    numbers = [int(x) for x in stuff[0].split(",")]
    lines = stuff[1].splitlines()
    wheels = [[] for _ in range(len(numbers))]
    i = 0
    for wl in range(3,len(lines[0]),4):
        for line in lines:
            target = line[wl-3:wl]
            if target == "   " or len(target) != 3: continue
            wheels[i].append(target)
        i += 1
    positions = [0]*len(numbers)
    print(wheels)
    MAX = dp(positions, 256, wheels, mode=max)
    cache.clear()
    MIN = dp(positions, 256, wheels, mode=min)
    print(f"{MAX} {MIN}")
    
# max = 606
