import sys
filename = sys.argv[1]

def find_h(row, word_):
    found = []
    for word in [word_, word_[::-1]]:
        for i in range(len(row)):
            positions = []
            for j in range(len(word)):
                pos = (i+j)%len(row)
                current = row[pos]
                if word[j] != current:
                    positions.clear()
                    break
                positions.append(pos)
            else:
                found.append(positions) 
    return found

def find_v(col_index, word_, grid):
    found = []
    m = len(grid)
    col = []
    for i in range(len(grid)):
        col.append(grid[i][col_index])
        
    for word in [word_, word_[::-1]]:
        for i in range(m):
            positions = []
            for j in range(len(word)):
                pos = (i+j)
                if pos >= len(col): break
                current = col[pos]
                if word[j] != current:
                    positions.clear()
                    break
                positions.append(pos)
            else:
                found.append(positions)
    return found


with open(filename) as f:
    i1, i2 = f.read().split("\n\n")
    words = i1.split(":")[1].split(",")
    grid =[list(x) for x in i2.splitlines()]
    seen = set()
    for j in range(len(grid[0])): # for each column
        for word in words:
            found = find_v(j, word, grid)
            for match in found:
                for x in match: seen.add((x, j))
    for i,row in enumerate(grid):
        for word in words:
            found = find_h(row, word)
            for match in found:                
                for y in match:
                    seen.add((i,y))
    print(len(seen))
