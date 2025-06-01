import math
sp = [list(map(float, i.split(' '))) for i in open('27a')]
n = 2
cl, ss = [[[] for _ in range(n)] for _ in range(2)]
it = []
for i in sp:
    if i[0] > 0.5:
        cl[0].append(i)
    else:
        cl[1].append(i)
for y in range(n):
    for i in cl[y]:
        s = 0
        for u in cl[y]:
            s += math.dist(i, u)
        ss[y].append(s)
    it.append(cl[y][ss[y].index(min(ss[y]))])
for i in range(2):
    print(int(sum([it[y][i] for y in range(n)]) / n * 10000))