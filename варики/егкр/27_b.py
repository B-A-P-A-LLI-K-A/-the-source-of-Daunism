import math
f = open('27_b')
cl = [[], [], []]
spc = [[], [], []]
sps = [[], [], []]
sp = [list(map(float, i.strip().split(' '))) for i in f]
for i in sp:
    if i[0] < 0:
        cl[0].append(i)
    elif i[1] > 7:
        cl[1].append(i)
    else:
        cl[2].append(i)
for y in range(3):
    for i in cl[y]:
        s = 0
        for u in cl[y]:
            s += math.dist(i, u)
        sps[y].append(s)
for y in range(3):
    spc[y] = cl[y][sps[y].index(min(sps[y]))]
px = 0
py = 0
for y in range(3):
    px += spc[y][0]
    py += spc[y][1]
print(int(px / 3 * 10000), int(py / 3 * 10000))