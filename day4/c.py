def compute(grid, m):
    return (sum([abs(m-x) for x in grid]))
    

with open("i3.txt") as f:
    grid = [int(x) for x in f.read().splitlines()]
    median = sorted(grid)[len(sorted(grid))//2]
    mean = sum(grid)//len(grid)
    print(f"median score: {compute(grid, median)}")
