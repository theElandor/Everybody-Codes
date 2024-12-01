name = "test.txt"
with open(name) as f:
    data= f.read().split("\n\n")
    words = data[0][6:].split(",")    
    s = data[1].split(" ")
    print(sum([s.count(w) for w in words]))