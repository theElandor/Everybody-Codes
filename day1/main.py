with open("input.txt") as f:    
    data = f.read()
    # data = "xBxAAABCDxCC"
    m = {"A":0, "B":1, "C":3, "D":5, "x":0}
    tot = 0
    for i in range(0,len(data)-2, 3): # x x x x x x x x
        j = i+1
        k = i+2        
        a,b,c, = data[i], data[j], data[k]
        g = "".join([a,b,c])
        print(g)
        if g.count("x") == 1:
            tot += 2
        elif g.count("x") == 0: 
            tot += 6
        tot += sum([m[x] for x in g])
    print(tot)