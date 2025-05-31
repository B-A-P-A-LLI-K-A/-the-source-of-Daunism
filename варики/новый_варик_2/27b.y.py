import math
sr = []
f = open('27b.x')
n = 3   #количество кластеров
cl = []
spr = []
for i in range(n):
    cl.append([])
    spr.append([])
for i in f:
    i = list(map(float, i.strip().split(' ')))
    ### распределение по кластерам
    if i[1] > 5:
        cl[0].append(i)
    elif i[1] > -5:
        cl[1].append(i)
    else:
        cl[2].append(i)
    ###
for i in range(len(cl)):
    for u in cl[i]:
        r = 0
        for y in cl[i]:
            r += math.dist(u, y)
        r /= len(cl[i])
        spr[i].append(r)
    sr.append(cl[i][spr[i].index(min(spr[i]))])
px = 0
py = 0
for i in range(len(sr)):
    px += sr[i][0]
    py += sr[i][1]
pxs = abs(int(px / len(sr) * 10000))
pys = abs(int(py / len(sr) * 10000))
print(pxs, pys)