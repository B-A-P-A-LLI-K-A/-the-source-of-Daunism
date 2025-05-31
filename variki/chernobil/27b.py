import math
sp = [list(map(float, i.split(' '))) for i in open('27b')]
b = 3
cl, ss = [[[] for _ in range(b)] for _ in range(2)]
it = []
for i in sp:
    if i[0] < -88:
        cl[0].append(i)
    elif i[1] < -5:
        cl[1].append(i)
    else:
        cl[2].append(i)
for y in range(b):
    for q in cl[y]:
        s = 0
        for w in cl[y]:
            s += math.dist(q, w)
        ss[y].append(s)
    it.append(cl[y][ss[y].index(min(ss[y]))])
for y in range(2):
    print(int(sum([it[u][y] for u in range(b)]) / b * 10000))