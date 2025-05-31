from itertools import product
from math import prod
def f(a, b, spp):
    if a == b:
        return 1
    elif a > b or a in spp:
        return 0
    else:
        return f(a + 1, b, spp) + f(a * 2, b, spp)


sp = [8, 19, 37, 42, 61]
w = []
s = 0
for n in range(2, 6):
    for i in product(sp, repeat=n):
        if sum([i.count(u) for u in i]) == len(i):
            q = list(i)
            q.sort()
            if not(q in w):
                w.append(q)
for i in w:
    o = [u for u in sp if not(u in i)]
    i.insert(0, 3)
    i.insert(len(i), 78)
    s += prod([f(i[p], i[p + 1], o) for p in range(len(i) - 1)])
print(s)