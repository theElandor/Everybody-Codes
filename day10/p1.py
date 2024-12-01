def fill(grid, i,j, seq):
	rows = set()
	for col in range(len(grid[0])):
		if grid[i][col] != ".":
			rows.add(grid[i][col])			
	for row in range(len(grid)):
		if grid[row][j] in rows:
			grid[i][j] = grid[row][j]
			seq.append(grid[row][j])
			break

with open("test.txt") as f:
	grid = [list(x) for x in f.read().splitlines()]
	for x in ["".join(x) for x in grid]:
		print(x)
	res = []
	m = len(grid)
	n = len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == ".":
				fill(grid, i, j, res)
	for x in ["".join(x) for x in grid]:
		print(x)
	print("".join(res))