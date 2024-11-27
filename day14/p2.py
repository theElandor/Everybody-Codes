mapping = {
    "U": (1,0,0),
    "D": (-1,0,0),
    "R": (0,1,0),
    "L": (0,-1,0),
    "F": (0,0,1),
    "B": (0,0,-1)
}
with open("input2.txt") as f:
    branches = [x.split(",") for x in f.read().splitlines()]
    print(branches)
    tot = set()
    for b in branches:
        current = (0,0,0)
        for c in b:
            d,n = c[0], int(c[1:])
            dx,dy,dz = mapping[d]
            for step in range(n):
                x,y,z = current
                tot.add((x+dx, y+dy, z+dz))
                current = (x+dx, y+dy, z+dz)
    print(len(tot))
                
