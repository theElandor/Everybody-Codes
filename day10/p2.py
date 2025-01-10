def print_grid(grid):
	for x in grid:
		print(x)

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

def convert(s):
	tot = 0
	for i,c in enumerate(s):
		tot += (ord(c)-ord('A')+1)*(i+1)
	return tot
		

with open("test.txt") as f:
	rows = f.read().split("\n\n")
	els = [[x.split(" ") for x in row.splitlines()] for row in rows]
	grids = [[[] for x in range(15)] for _ in range(7)]
	# grids shape 7,15
	for i,brow in enumerate(els):
		for j,row in enumerate(brow):
			for k,single in enumerate(row):
				grids[i][k].append(single)
	print_grid(grids[0][0])
	final = []
	for r in grids:
		for c in r:
			grid = [list(x) for x in c]
			m = len(grid)
			n = len(grid[0])
			res = []
			for i in range(m):
				for j in range(n):
					if grid[i][j] == ".":
						fill(grid, i, j, res)
			print("".join(res))
			final.append(res)
	print([convert(x) for x in final])
	print(sum([convert(x) for x in final]))
	print(convert("A"))