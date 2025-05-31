f = open('19878.txt')
sp = []
kol = 0
for i in f:
    sp.append(list(map(int, i.split(' '))))
for i in sp:
    sp1 = []
    sp2 = []
    sp3 = []
    for x in i:
        sp1.append(i.count(x))
    for x in range(len(sp1)):
        if sp1[x] != 1:
            sp2.append(x)
    for x in sp2:
        sp3.append(i[x])
    sp3 = set(sp3)
    sp3 = list(sp3)
    for t in sp3:
        while i.count(t) > 0:
            i.remove(t)
    sr = sum(i) / len(i)
    sp1.sort()
    print(i, sp3, sp1)
    if sp1 == [1, 1, 1, 1, 3, 3, 3]:
        if len(sp3) == 1:
            if sr <= sp3[0]:
                kol += 1
print(kol)
