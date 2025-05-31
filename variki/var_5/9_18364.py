def g(z):
    c = 1
    for o in z:
        c *= o
    return c


f = open('9_18364.txt')
sp = []
kol = 0
for i in f:
    sp.append(list(map(int, i.split(' '))))
for i in sp:
    spp = []
    spq = []
    spw = []
    for x in i:
        spp.append(i.count(x))
    for x in range(len(spp)):
        if spp[x] != 1:
            spq.append(x)
    for x in spq:
        spw.append(i[x])
    if len(spw) != 0:
        for t in spw:
            for p in range(i.count(t)):
                i.remove(t)
    if 3 * sum(i) <= g(spw):
        kol += 1
print(kol)
