sp = [list(map(int, i.split(' '))) for i in open('yandex.1')]
kol = 0
for i in sp:
    k = 0
    s = [i.count(u) for u in i]
    s.sort()
    if s == [1, 1, 1, 3, 3, 3]:
        k += 1
    sc = [u for u in i if u % 2 == 0]
    sn = [u for u in i if u % 2 == 1]
    if len(sc) > len(sn):
        k += 1
    o = i.copy()
    o.sort()
    if sum(o[-2:]) > 2 * (sum(o[:-2])):
        k += 1
    if k > 1:
        kol += 1
print(kol)