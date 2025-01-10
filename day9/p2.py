import sys
# stupid bug, set difference loop to 50 instead of 100
sys.setrecursionlimit(10000000)
def gen(dots,w):
    dp = [0]*(w+1)
    for i in range(1,w+1):
        choices = []
        for d in dots:
            if d <= i:
                choices.append(1+dp[i-d])
        dp[i] = min(choices)
    return dp

with open("test.txt") as f:
    dots = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
    betles = [int(x) for x in f.read().splitlines()]
    tot = 0
    max_b = max(betles)        
    dp = gen(dots, max_b)
    print("done")    
    for n in betles:        
        choices = []
        p1 = n // 2
        if n % 2 == 0:
            for i in range(50):
                choices.append(dp[p1-i]+dp[p1+i])
        else:            
            for i in range(50):
                choices.append(dp[p1-i]+dp[p1+i+1])
        tot += min(choices)
    print(tot)