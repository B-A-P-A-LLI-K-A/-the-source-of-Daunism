f = [list(map(int, i.split(' '))) for i in open('7674.txt')]
k = 0
for i in f:
    sp = [i.count(o) for o in i]
    sp.sort()
    if sp == [1, 1, 1, 2, 2]:
        sp = [i.count(o) for o in i]
        if (sum([i[p] for p in range(5) if sp[p] == 1]) / 3) < (sum([i[p] for p in range(5) if sp[p] == 2]) / 2):
            k += 1
print(k)