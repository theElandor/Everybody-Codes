def get(n,a,b):
    heights = [1]
    w = 1 
    current = 1
    h = 1
    t = 1
    while b > 0:
        w = w + 2
        t = ((t * n)%a)+a
        current = t*w
        b -= current
        h += 1
        new_h = []
        new_h.append(t)
        for i in range(len(heights)):
            new_h.append(heights[i] + t)
        new_h.append(t)        
        heights = new_h
    return abs(b), w, heights
n = 988272
b = 202400000
a = 10

# n = 2
# a = 5
# b = 160
b_needed, final_w, heights = get(n,a,b)
print(heights)
tot = 0
for i in range(1, len(heights)-1):
    tot += (n*final_w*heights[i])%a
needed_final = ((b+1)+abs(b_needed))-tot
print(abs(b - needed_final))