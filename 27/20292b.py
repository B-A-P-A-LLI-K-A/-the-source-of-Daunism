f = open('20292b')
sp = []
cl = [[], [], [], [], [], [], []]
ss = []
for i in f:
    sp.append(list(map(float, i[:-1].split(' '))))

for i in sp:
    if i[0] < 1:
        if i[0] < -4:
            cl[0].append(i)
        elif i[1] > -2:
            cl[1].append(i)
        else:
            cl[2].append(i)
    else:
        if i[1] > 1:
            if i[0] > 6:
                cl[3].append(i)
            else:
                cl[4].append(i)
        else:
            if i[0] > 6:
                cl[5].append(i)
            else:
                cl[6].append(i)

for i in range(7):
    s = 0
    for p in cl[i]:
        for u in cl[i]:
            if p != u:
                s += ((p[0] - u[0]) ** 2 + (p[1] - u[1]) ** 2) ** 0.5
    print(s, len(cl[i]), cl[i])
    ss.append(s / (len(cl[i]) * (len(cl[i]) - 1)))
print(int(min(ss) * 100000), int(max(ss) * 100000))
