from collections import deque
with open("test.txt") as f:
	grid = f.read().splitlines()
	q = deque()
	initial = []
	for line in grid:
		initial.append(line.split(":")[0])
	print(f"trying {initial[0]}")
	q.append(initial[0])
	for day in range(20):
		to_add = []
		#print(day)
		while len(q):
			#print(q)
			current = q.popleft()
			for line in grid:
				#print(line)
				dead, gen = line.split(":")[0], line.split(":")[1].split(",")
				if dead == current:
					for termite in gen:
						to_add.append(termite)
		for item in to_add:
			q.append(item)
	print(len(q))
	# for el in q:
	# 	print(el, end=",")