import math
f = open('27_a')
x = 2
cl = [[] for _ in range(x)]
spc = [[] for _ in range(x)]
sps = [[] for _ in range(x)]
sp = [list(map(float, i.strip().split(' '))) for i in f]
for i in sp:
    if i[1] > 6:
        cl[0].append(i)
    else:
        cl[1].append(i)
for y in range(2):
    for i in cl[y]:
        s = 0
        for u in cl[y]:
            s += math.dist(i, u)
        sps[y].append(s)
for y in range(2):
    spc[y] = cl[y][sps[y].index(min(sps[y]))]
px = 0
py = 0
for y in range(2):
    px += spc[y][0]
    py += spc[y][1]
print(int(px / 2 * 10000), int(py / 2 * 10000))