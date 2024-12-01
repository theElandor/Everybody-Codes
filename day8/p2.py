# n = 722
# a = 1111
# b = 20240000-1
n = 3
a = 5
b = 50-1
w = 1 
current = 1
h = 1
it = 2
t = 1
while b > 0: 
    w = w + 2
    t = (t * n)%a
    current = t*w
    b -= current
    h += 1
# print(abs(b)*w)
print(abs(b), w)