from copy import deepcopy
import sys
# parsing problem, took me 30 years
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
filename = sys.argv[1]
spins = int(sys.argv[2])
with open(filename) as f:    
    stuff = f.read().split("\n\n")
    numbers = [int(x) for x in stuff[0].split(",")]
    print(len(numbers))
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
    seen = {}
    t = 0
    coins = 0
    while t <= spins:
        for i in range(len(positions)):
            positions[i] = (positions[i]+numbers[i])%len(wheels[i])
        state = tuple(positions)
        faces = []
        for i, w in enumerate(wheels):
            faces.append(w[state[i]])
        coins += get_coins("".join([x[0]+x[2] for x in faces]))
        if state in seen:
            ot, oc, = seen[state]
            dt, dc = t-ot, coins-oc
            have_to_do = spins-t
            loops = (have_to_do // dt)
            coins += (loops * dc)
            spins_left = have_to_do % dt
            t = spins - spins_left + 1
        else:
            seen[state] = (t, coins)
            t += 1
    print(coins)
