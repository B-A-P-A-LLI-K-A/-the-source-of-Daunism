sp = [list(map(int, i.split())) for i in open('9')]
k = 0
for i in sp:
    pp = [i.count(u) for u in i]
    o = pp.copy()
    pp.sort()
    if pp != [1, 1, 1, 3, 3, 3]:
        q = 0
        w = 0
        for u in range(len(i)):
            if o[u] == 1:
                q += i[u]
            else:
                w += (i[u] ** 2)
        if q ** 2 >= w:
            k += 1
print(k)#ответ правильный, но на КЕГЭ отмечен как неверный