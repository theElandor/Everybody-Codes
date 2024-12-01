from copy import deepcopy
import sys
filename = sys.argv[1]
spins = int(sys.argv[2])
if filename == "test.txt":
    circles = 3
else:
    circles = 4
with open(filename) as f:
    stuff = f.read().split("\n\n")
    numbers = [int(x) for x in stuff[0].split(",")]
    data = stuff[1].splitlines()
    sets = {i:[] for i in range(circles)}
    nd = []
    for line in data:
        faces = line.split(" ")
        removing = False
        r = 0
        for i in range(len(faces)):
            if faces[i] == "" and not removing:
                faces[i] = "#"
                removing = True
            elif faces[i] != "":
                removing = False
            elif faces[i] == "" and removing:
                r+=1
                if r == 3:
                    removing = False
        while "" in faces:
            faces.remove("")
        for i, face in enumerate(faces):
            if face != "#": sets[i].append(face)
        nd.append(faces)
    for r in nd:
        print(r)
    coins = 0
    current = nd[0]
    pos = [0,0,0] if filename == "test.txt" else [0,0,0,0]
    for key,val in sets.items():
        print(key, val)
    for t in range(spins):
        new = []
        for i,(face,n) in enumerate(zip(current, numbers)):
            nextpos = (pos[i]+n)%len(sets[i])
            new_face = sets[i][nextpos]
            new.append(new_face)
            pos[i] = nextpos
        current = deepcopy(new)
    print(" ".join(new))
