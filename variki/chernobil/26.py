sp = [list(map(int, i.split(' '))) for i in open('26')]
n = sp[0]
sp.pop(0)
sp.sort()
ss = [[i[0] + 1, i[0] + i[1] + 1] for i in sp]
z, ot, s = [0, 0, 0]
spd = []
for k in range(1, 1441):
    while k in spd:
        spd.remove(k)
        z -= 1
    for i in ss:
        if k == i[0]:
            if z <= 24:
                spd.append(i[1])
                z += 1
            else:
                ot += 1
    if z < 13:
        s += 1
print(ot, s)