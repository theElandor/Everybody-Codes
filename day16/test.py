from copy import deepcopy
import sys

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
    data = stuff[1].splitlines()
    print(stuff)
