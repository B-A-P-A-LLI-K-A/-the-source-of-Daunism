f = open('20295a3')
l = []
ks = []
for i in f:
    l.append(list(map(float, i.split())))
for i in l:
    x1 = i[0]
    y1 = i[1]
    k = 0
    for t in l:
        x2 = t[0]
        y2 = t[1]
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if r <= 1:
            k += 1
    ks.append(k)
sr = (sum(ks) / len(ks))
print(sr)
