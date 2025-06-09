from math import dist
sp = [list(map(float, i.split())) for i in open('21930_b')]
x = 3
cl, sps = [[[] for _ in range(x)] for _ in range(2)]
it = []
for i in sp:
    if i[1] < 10:
        cl[0].append(i)
    elif i[0] > 17:
        cl[1].append(i)
    else:
        cl[2].append(i)
for y in range(x):
    for i in cl[y]:
        s = 0
        for u in cl[y]:
            s += dist(i, u)
        sps[y].append(s)
    it.append(cl[y][sps[y].index(max(sps[y]))])
for i in range(2):
    print(int(sum([it[p][i] for p in range(x)]) / x * 10000))