import sys
filename = sys.argv[1]
t = open("track.txt")
f = open(filename)
track = t.read().splitlines()
print(track)
r,l = [], []
for line in track[1:-1]:
    r.append(line[-1])
    l.append(line[0])
track = track[0]+"".join(r)+track[-1][::-1]+"".join(l)
track = track[1:]+"S"
strats = f.read().splitlines()
scores = []
print(track)
for s in strats:
    score = 0
    letter, commands = s.split(":")[0], s.split(":")[1].split(",")
    fuel = 10
    print(letter)
    for pos in range(0, len(track)*10):
        test = commands[pos%len(commands)]
        forced = track[pos%len(track)]        
        if forced == "=" or forced == "S": c = test
        else: c = forced
        print(c, end="")
        if c == "+":
            fuel += 1
        elif c == "-":
            fuel -= 1
        score += fuel
    scores.append((score, letter))    
print(scores)
so = sorted(scores, key=lambda x:x[0], reverse=True)
print("".join([y for x,y in so]))

t.close()
f.close()
