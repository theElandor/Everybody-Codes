#!/usr/bin/python3 
import sys
from collections import defaultdict, deque, Counter
import heapq
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'A.in'
G = open(infile).read().strip()
xs, faces = G.split('\n\n')
xs = [int(x) for x in xs.split(',')]
print(xs)
print(faces)

nc = (len(faces.split('\n')[0]) + 1) // 4
C = [[] for _ in range(nc)]

for line in faces.split('\n'):
    row = []
    for i in range(nc):
        face = line[i*4:i*4+3]
        if face.strip():
            C[i].append(face)
#print(' '.join(C[i][(xs[i]*100)%len(C[i])] for i in range(nc)))

N = 202420242024
state = [0 for _ in range(nc)]
t = 0
ans = 0
DP = {}
while t < N:
    t += 1
    new_state = [(state[i]+xs[i])%len(C[i]) for i in range(nc)]
    state = new_state
    key = tuple(state)
    if key in DP:
        dt = t-DP[key][0]
        dans = ans-DP[key][1]
        amt = (N - t) // dt
        t += amt*dt
        ans += amt*dans
    else:
        DP[key] = (t, ans)

    score = Counter()
    for i in range(nc):
        face = C[i][new_state[i]]
        score[face[0]] += 1
        score[face[2]] += 1
    score = sum(max(0, v-2) for v in score.values())
    ans += score
    print(f'{t=} {ans=}')
