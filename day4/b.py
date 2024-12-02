with open("i2.txt") as f:
    grid = [int(x) for x in f.read().splitlines()]
    m = min(grid)
    print(sum([abs(m-x) for x in grid]))
