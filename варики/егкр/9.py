f = open('9')
sp = []
for i in f:
    sp.append((list(map(int, i.strip().split(' ')))))
for i in range(len(sp)):
    e = sp[i]
    r = [e.count(o) for o in e]
    a = r.copy()
    a.sort()
    if a == [1, 3, 3, 3, 3, 3, 3]:
        z = e[r.index(1)]
        if ((sum(e) - z) / 6) < z:
            print(i + 1)
