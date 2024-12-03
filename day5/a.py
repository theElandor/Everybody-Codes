# super annoying modulo operations.
# Took me longer then expected.
# This file contains all of the three parts.

with open("i3.txt") as f:
    grid = [[int(x) for x in y.split()] for y in f.read().splitlines()]
    lines = []
    for j in range(len(grid[0])):
        line = []
        for i in range(len(grid)):
            line.append(grid[i][j])
        lines.append(line)
    r = 0
    shouts = {}
    m = -1
    while True:
        source, target = r%len(lines), (r+1)%len(lines)
        sline, tline = lines[source], lines[target]
        element = sline[0]
        p = element-1
        side = (p // (len(tline)))%2
        pos = p % len(tline) if side == 0 else len(tline) - (p % len(tline))
        tline.insert(pos, element)
        del sline[0]
        n = "".join([str(l[0]) for l in lines])
        if n in shouts: shouts[n] += 1
        else: shouts[n] = 1
        #print(f"{r+1}, {n}")
        m = max(m, int(n))
        print(m)
        # if shouts[n] == 2024:
        #     print(f"ans found: {n}")
        #     print(int(n) * (r+1))
        #     break
        r+=1
