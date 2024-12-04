import sys
filename = sys.argv[1]
with open(filename) as f:
    strats = f.read().splitlines()
    scores = []
    for s in strats:
        score = 0        
        letter, commands = s.split(":")[0], s.split(":")[1].split(",")
        fuel = 10
        p = 0
        for segment in range(10):
            c = commands[p%len(commands)]
            if c == "+":
                fuel += 1
            elif c == "-":
                fuel -= 1
            score += fuel
            p += 1
        scores.append((score, letter))
    so = sorted(scores, key=lambda x:x[0], reverse=True)
    print("".join([y for x,y in so]))