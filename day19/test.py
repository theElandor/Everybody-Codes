import sys
filename = sys.argv[1]
with open(filename) as f:
    data = f.read().split("\n\n")
    ops = data[0]
    grid = [list(x) for x in data[1].splitlines()]
    numbers = []
    m = len(grid)
    n = len(grid[0])    
    for i in range(m):
        for j in range(n):
            if grid[i][j].isdigit() and grid[i][j] != "0":
                numbers.append(grid[i][j])
    print("".join(numbers))
    counter = {x:numbers.count(x) for x in numbers}
    for k,v in counter.items():
        print(f"{k}--> {v}")
    
