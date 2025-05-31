import math
sp = [list(map(float, i.strip().split(' '))) for i in open('27_b')]
x = 3
cl, sps = [[[] for _ in range(x)] for _ in range(2)]
c = []
for i in sp:
    if i[1] > 10:
        cl[0].append(i)
    elif i[0] > 10:
        cl[1].append(i)
    else:
        cl[2].append(i)
for i in range(x):
    for q in cl[i]:
        s = 0
        for w in cl[i]:
            s += math.dist(q, w)
        sps[i].append(s)
    c.append(cl[i][sps[i].index(min(sps[i]))])
print(c)
for i in range(2):
    print(int(sum([c[y][i] for y in range(x)]) / x * 10000))