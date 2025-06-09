cl = []
for i in range(1, 100000):
    s = int(str(i) + '777')
    p = 0
    for u in range(2, int(s ** 0.5) + 1):
        if s % u == 0:
            p = 1
            break
    if p == 0:
        cl.append(s)
k = 0
for i in range(55000001, 100000000):
    c = 0
    for u in cl:
        if i % u == 0:
            c = 1
            break
    if c == 1:
        print(i, u)
        k += 1
    if k == 4:
        break