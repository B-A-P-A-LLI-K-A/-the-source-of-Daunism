sp = [list(map(int, i.split(' '))) for i in open('yandex.2')]
k = 0
for i in sp:
    o = [i.count(u) for u in i]
    a = o.copy()
    a.sort()
    if a == [1, 1, 1, 3, 3, 3]:
        if (i[o.index(3)] * 3) ** 2 > (sum(i) - 3 * i[o.index(3)]) ** 2:
            k += 1
print(k)