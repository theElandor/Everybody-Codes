def merge(intervals):
    if len(intervals) == 0:
        return [],0
    sl = sorted(intervals, key= lambda x:x[0])
    cs, ce = sl[0]
    merged = []
    for s, e in sl[1:]:
        if s <= ce:
            ce = max(e, ce)
        else:
            merged.append((cs,ce))
            cs, ce = s,e
    merged.append((cs,ce))
    res = sum(e-s for s,e in merged)
    return merged, res

intervals = [[1,3], [3,5], [5,7],[7,8],[7,8],[7,22], [8,17]]
print(merge(intervals))