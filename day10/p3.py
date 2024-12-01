import sys
from copy import deepcopy
def fill(grid, i,j, rs, cs):
	rows = set()
	for col in range(cs, cs+8):
		if grid[i][col] not in [ ".","?"] :
			rows.add(grid[i][col])			
	for row in range(rs, rs+8):
		if grid[row][j] in rows:
			grid[i][j] = grid[row][j]
			break
                
def solve(grid, i,j, rs, cs):
	f = {}
	for col in range(cs, cs+8):
		c = grid[i][col]
		f[c] = f[c] +1 if c in f else 1
	for row in range(rs, rs+8):
		c = grid[row][j]
		f[c] = f[c] +1 if c in f else 1
	# find single one
	s = [k for k,v in f.items() if (v < 2 and k != "?")]
	if len(s) != 1:
		return False
	print(f)
	# -----------------
	# crazy: I tried to find this shit bug
	# for like 3 days in a row, then randomly
	# tried a day later, and immediately found the solution.
	# I think there is always some thread in our memory that
	# works on unsolved problems...now I believe in people
	# that say that if you become to obsessed with a problem
	# you won't be able to see the solution anymore.
	if "?" not in f or f["?"] != 1:
		grid[i][j] = s[0]
	# -----------------
	for col in range(cs, cs+8):
		if grid[i][col] == "?":
			grid[i][col] = s[0]
			return True
	for row in range(rs, rs+8):
		if grid[row][j] == "?":
			grid[row][j] = s[0]
			return True
	return True


def convert(s):
	tot = 0
	for i,c in enumerate(s):
		tot += (ord(c)-ord('A')+1)*(i+1)
	return tot

if len(sys.argv) != 2:
	print("provide input!")
	exit(0)
name = sys.argv[1]

def print_grid(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			print(grid[i][j], end="")
		print("")

def check(grid, rs, cs):
	for i in range(rs, rs+8):
		for j in range(cs, cs+8):
			if grid[i][j] == "?" or grid[i][j]== ".":
				return False
	for i in range(rs+2,rs+6):
		for j in range(cs+2,cs+6):
			current = grid[i][j]
			if current != "*":
				row_counter = 0
				for jj in range(cs, cs+8):
					c = grid[i][jj]
					if c == current:
						row_counter += 1
				col_counter = 0
				for ii in range(rs, rs+8):
					c = grid[ii][j]
					if c == current:
						col_counter += 1
				if col_counter == 2 and row_counter == 2:
					continue
				else:
					return False
	return True

with open(name) as f:
	grid = [list(x) for x in f.read().splitlines()]
	ci = []
	ri = []
	i = 0
	print(len(grid[0]))
	while (6*i)+8 <= len(grid[0]):
		ci.append((6*i,6*i+ 8))
		i+=1
	i = 0
	while (6*i)+8 <= len(grid):
		ri.append((6*i,6*i+ 8))
		i+=1	
	# grids = []
	times = 0
	while(True):
		prev_grid = deepcopy(grid)
		print(times)
		# for each subgrid
		for rs,re in ri:
			for cs, ce in ci:
				# fill
				for i in range(8):
					for j in range(8):
						if grid[rs+i][cs+j] == ".":
							fill(grid , rs+i, cs+j, rs, cs)
				for i in range(8):
					for j in range(8):
						if grid[i+rs][j+cs] == ".":
							solve(grid,rs+i,cs+j, rs, cs)
		if grid == prev_grid:
			print(f"Loops: {times+1}")
			break
		times += 1
	print_grid(grid)
	total = 0
	for rs, re in ri:
		for cs, ce in ci:
			runes = [[grid[rs+ii][cs+jj] for jj in range(2,6)] for ii in range(2,6)]
			test = ""
			for row in runes:
				for col in row:
					test += col
			if check(grid, rs, cs):
				score = convert(test)
				total += score
	print(total)
