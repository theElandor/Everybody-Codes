from collections import deque
import sys
filename = sys.argv[1]
with open(filename) as f:
    nodes = f.read().splitlines()
    G = {}
    for line in nodes:
        source, dests = line.split(":")[0], line.split(":")[1].split(",")
        G[source] = dests
    Q = deque()
    Q.append((0,"RR", "R")) #dist, current, path
    prev = None
    d = {}
    while Q:
        dist, current, path = Q.popleft()
        if current == "@":
            if dist not in d:
                d[dist] = [path]
            else:
                d[dist].append(path)
        if current in G:
            for v in G[current]:
                Q.append((dist+1, v, path+v[0]))
        for k,v in d.items():
            if len(v) == 1: print(v)