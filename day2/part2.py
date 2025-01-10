import sys
import re
if len(sys.argv) != 2:
    exit(0)
name = sys.argv[1]
def search(pattern, target, position):
    for i in range(len(pattern)):
        if pattern[i] != target[i+position]:
            return False
    return True
with open(name) as f:
    data= f.read().split("\n\n")
    inscr = data[0][6:].split(",")
    words = inscr + [x[::-1] for x in inscr]
    insc = data[1].splitlines()
    tot = 0
    print(words)
    for target in insc:        
        bag = set()
        for w in words:
            starts = []
            for i in range(len(target)-len(w)+1):
                if search(w, target, i):
                    starts.append(i)
            for start in starts:
                for j in range(len(w)):                    
                    bag.add(start+j)
        #print(f"{target} -> {bag}")
        tot += len(bag)
    print(tot)