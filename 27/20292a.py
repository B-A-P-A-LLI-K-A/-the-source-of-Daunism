f = open('20292a')
sp = []
cl = [[], [], [], []]
ss = []
for i in f:
    sp.append(list(map(float, i[:-1].split(' '))))

for i in sp:
    if i[0] < 2:
        if i[1] > 0:
            cl[0].append(i)
        else:
            cl[1].append(i)
    elif i[1] > 2:
        cl[2].append(i)
    else:
        cl[3].append(i)

for i in range(4):
    s = 0
    for p in cl[i]:
        for u in cl[i]:
            if p != u:
                s += ((p[0] - u[0]) ** 2 + (p[1] - u[1]) ** 2) ** 0.5
    ss.append(s / (len(cl[i]) * (len(cl[i]) - 1)))
print(int(min(ss) * 100000), int(max(ss) * 100000))
