from math import dist
sp = [list(map(float, i.split(' '))) for i in open('27_b')]
n = 3
cl, ss = [[[] for _ in range(n)] for _ in range(2)]
ot = []
for i in sp:
    if i[0] < 10:
        cl[0].append(i)
    elif i[0] > 20:
        cl[1].append(i)
    else:
        cl[2].append(i)
for y in range(n):
    for i in cl[y]:
        s = 0
        for u in cl[y]:
            s += dist(i, u)
        ss[y].append(s)
    ot.append(cl[y][ss[y].index(min(ss[y]))])
for y in range(2):
    print(int(sum([ot[u][y] for u in range(n)]) / n * 10000))
print(ot)