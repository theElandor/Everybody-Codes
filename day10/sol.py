import sys
from collections import Counter
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'C.in'
G_BIG = open(infile).read().strip()
G_BIG = G_BIG.split('\n')
G_BIG = [[c for c in row] for row in G_BIG]
#assert len(G_BIG[-1]) == 0
#G_BIG.pop()

for i, row in enumerate(G_BIG):
    assert len(row) == len(G_BIG[0]), f'{len(row)=} {len(G_BIG[0])=} {row=} {i=}'

R = 8
C = 8

t = 0
count = 0
while True:
    t += 1
    changed = False
    for br in range(0, len(G_BIG), 6):
        if br+R-1>=len(G_BIG):
            continue
        for bc in range(0, len(G_BIG[br]), 6):
            if bc+C-1>=len(G_BIG[br]):
                continue

            count += 1

            block = ''
            G = [[G_BIG[br+r][bc+c] for c in range(C)] for r in range(R)]
            i = 0
            for r in range(R):
                for c in range(C):
                    if G[r][c] == '.':
                        row = {G[r][cc] for cc in range(C)}
                        col = {G[rr][c] for rr in range(R)}
                        final = row & col
                        final.discard('.')
                        final.discard('?')
                        i += 1
                        if len(final) == 1:
                            ch = list(final)[0]
                            G_BIG[br+r][bc+c] = ch
                            changed = True
            for r in range(R):
                for c in range(C):
                    if G[r][c] == '?':
                        row = {G[r][cc] for cc in range(C)}
                        col = {G[rr][c] for rr in range(R)}
                        if '*' not in row:
                            dots = [cc for cc in range(C) if G[r][cc]=='.']
                            if len(dots) == 1:
                                dot_col = Counter(G[rr][dots[0]] for rr in range(R))
                                opts = [k for k,v in dot_col.items() if v==1 and k!='.']
                                if len(opts) == 1:
                                    G_BIG[br+r][bc+c] = list(opts)[0]
                                    changed = True
                        if '*' not in col:
                            dots = [rr for rr in range(R) if G[rr][c]=='.']
                            if len(dots) == 1:
                                dot_row = Counter(G[dots[0]][cc] for cc in range(C))
                                opts = [k for k,v in dot_row.items() if v==1 and k!='.']
                                if len(opts) == 1:
                                    G_BIG[br+r][bc+c] = list(opts)[0]
                                    changed = True
    if not changed:
        break

ans = 0
for br in range(0, len(G_BIG), 6):
    if br+R-1>=len(G_BIG):
        continue
    for bc in range(0, len(G_BIG[br]), 6):
        if bc+C-1>=len(G_BIG[br]):
            continue
        G = [[G_BIG[br+r][bc+c] for c in range(C)] for r in range(R)]
        ok = True
        block_score = 0
        i = 0
        for r in [2,3,4,5]:
            for c in [2,3,4,5]:
                if G[r][c] == '.' or G[r][c]=='?':
                    ok = False
                else:
                    ch_int = ord(G[r][c])-ord('A')+1
                    assert 1<=ch_int<=26
                    i += 1
                    block_score += i*ch_int
        if ok:
            print(f'{br=} {bc=} {block_score=}')
            ans += block_score

for row in G_BIG:
    print(''.join(row))
print(t)
print(ans)