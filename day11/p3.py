from collections import deque
with open("input.txt") as f:
	results = []
	grid = f.read().splitlines()
	q = deque()
	initial = []
	for line in grid:
		initial.append(line.split(":")[0])
	print(f"trying {initial[0]}")
	for t in initial:
		total = {t:1}
		for day in range(20):
			current = {}
			for key, val in total.items():
				for line in grid:
					dead, gen = line.split(":")[0], line.split(":")[1].split(",")					
					if dead == key:
						for g in gen:
							if g not in current:
								current[g] = val
							else:
								current[g] += val
			total = current
		results.append(sum([v for k,v in total.items()]))

	print(max(results)-min(results))
	# for el in q:
	# 	print(el, end=",")