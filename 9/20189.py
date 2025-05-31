f = open('20189')
sp = []
for i in f:
    sp.append(list(map(int, i.strip().split(' '))))
for i in sp:
    se = set(i)
    if len(se) == 5:
        for p in range(5):
            i.remove(se[p])
