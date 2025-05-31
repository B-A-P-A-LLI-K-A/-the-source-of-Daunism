import math
x = 2
cl, sps = [[[] for _ in range(x)] for _ in range(2)]
sr = [0, 0]
sp = [(list(map(float, i.strip().split(' ')))) for i in open('20816_a')]
for i in sp:
    if i[0] > 0:
        cl[0].append(i)
    else:
        cl[1].append(i)
for t in range(x):
    for i in cl[t]:
        s = 0
        for u in cl[t]:
            s += math.dist(i, u)
        sps[t].append(s)
    for r in range(2):
        sr[r] += cl[t][sps[t].index(min(sps[t]))][r]
print([abs(int(i / x * 10000)) for i in sr])