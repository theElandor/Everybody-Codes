with open("test.txt") as f:
    dots = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
    betles = [int(x) for x in f.read().splitlines()]
    tot = 0
    print(betles)
    for b in betles:
        current = len(dots)-1        
        print(f"b: {b}")
        while b > 0:
            cd = dots[current]            
            if b >= cd:
                print(cd)
                b -= cd
                tot += 1
            else:
                current -= 1
    print(tot)
        
