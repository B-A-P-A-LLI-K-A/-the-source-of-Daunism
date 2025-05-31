sp = [list(map(int, i.strip().split(' '))) for i in open('9')]
k = 0
for i in sp:
    spp = [i.count(o) for o in i]
    o = i.copy()
    a = spp.copy()
    spp.sort()
    if spp == [1, 3, 3, 3, 3, 3, 3]:
        o.pop(a.index(1))
        if i[a.index(1)] < max(o):
            k += 1
print(k)