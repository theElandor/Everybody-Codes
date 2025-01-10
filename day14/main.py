with open("input.txt") as f:
    high = 0
    commands = [(x[0],x[1:]) for x in f.read().strip().split(",")]
    current = 0 
    print(commands)
    for d, n in commands:
        if d == "D":
            current -= int(n)
        elif d == "U":
            current += int(n)
        high = max(high, current)
    print(high)
