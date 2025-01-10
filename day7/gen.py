paths = []
def gen_paths(p,m,e, current="") -> list:
    prev = current
    if p == 0 and m == 0 and e == 0:
        paths.append(current)
    if p > 0:
        current += "+"
        gen_paths(p-1, m, e, current)
        current = prev
    if m > 0:
        current += "-"
        gen_paths(p, m-1, e, current)
        current = prev
    if e > 0:
        current += "="
        gen_paths(p, m, e-1, current)

gen_paths(5,3,3)
print(len(paths))
