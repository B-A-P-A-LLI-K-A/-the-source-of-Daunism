import math
f = open('20816_b')
x = 3
cl, sps, c = [[[] for _ in range(x)] for _ in range(3)]
sr = [0, 0]
sp = [(list(map(float, i.strip().split(' ')))) for i in f]
for i in sp:
    if i[1] > -1:
        cl[0].append(i)
    elif i[0] < -5:
        cl[1].append(i)
    else:
        cl[2].append(i)
for t in range(x):
    for i in cl[t]:
        s = 0
        for u in cl[t]:
            s += math.dist(i, u)
        sps[t].append(s)
    for r in range(2):
        sr[r] += cl[t][sps[t].index(min(sps[t]))][r]
print([abs(int(i / x * 10000)) for i in sr])